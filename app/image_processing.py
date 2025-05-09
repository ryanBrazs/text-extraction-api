from PIL import Image
import io
import cv2
import numpy as np
import pytesseract
from google.cloud import vision
from .config import credentials
from .text_processing import process_text

# Inicializa o cliente da API com as credenciais
client = vision.ImageAnnotatorClient(credentials=credentials)

def resize_image(image_file, max_size=(300, 300), quality=75):
    try:
        img = Image.open(image_file)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)
        return buffer.getvalue(), img
    except Exception as e:
        print(f"Erro ao redimensionar imagem: {e}")
        image_file.seek(0)
        return image_file.read(), None

def convert_to_black_and_white(img):
    img_np = np.array(img.convert('L'))
    _, bw_img = cv2.threshold(img_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(bw_img)

def detect_text_pytesseract(img):
    """Detecta texto em uma imagem usando pytesseract."""
    try:
        # Converte a imagem para preto e branco
        bw_img = convert_to_black_and_white(img)
        # Configuração otimizada para velocidade
        custom_config = r'--oem 1 --psm 6 -l por -c tessedit_do_invert=0'
        text = pytesseract.image_to_string(bw_img, config=custom_config)
        return process_text(text)
    except Exception as e:
        print(f"Erro no pytesseract: {e}")
        return "", ""

def detect_text_google(image_content):
    """Detecta texto em uma imagem usando a API do Google Cloud Vision."""
    image = vision.Image(content=image_content)
    try:
        response = client.text_detection(image=image, timeout=5.0)
    except Exception as e:
        raise Exception(f'Erro na API: {e}')

    if response.error.message:
        raise Exception(f'Erro na API: {response.error.message}')

    text = response.text_annotations[0].description if response.text_annotations else ''
    return process_text(text)

def detect_text(image_file):
    """Tenta detectar texto usando pytesseract primeiro, depois Google Cloud Vision se necessário."""
    # Redimensiona a imagem
    image_content, img = resize_image(image_file, max_size=(512, 512), quality=75)
    
    # Tenta com pytesseract se a imagem foi carregada corretamente
    if img:
        text, matched_medication = detect_text_pytesseract(img)
        if matched_medication:
            return text, matched_medication
    
    # Usa Google Cloud Vision como fallback
    return detect_text_google(image_content)