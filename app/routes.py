from flask import Blueprint, request, jsonify
from .image_processing import detect_text

bp = Blueprint('routes', __name__)

@bp.route('/detect-text', methods=['POST'])
def detect_text_endpoint():
    """Endpoint para detectar texto em uma imagem enviada."""
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem enviada'}), 400

    image_file = request.files['image']
    
    try:
        # Processa a imagem
        detected_text, matched_medication = detect_text(image_file)
        
        # Prepara a resposta
        response = {
            'matched_medication': matched_medication if matched_medication else 'Nenhum medicamento identificado'
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500