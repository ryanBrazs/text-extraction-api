import nltk
from unidecode import unidecode
import re

# Baixa os recursos necessários do NLTK (executado apenas na inicialização)
nltk.download('punkt')
nltk.download('punkt_tab')

# Pré-processa a lista de stopwords como conjunto para busca mais rápida
stopwords = {
    'ems', 'eurofarma', 'sandoz', 'novartis', 'pfizer', 'sanofi', 'ache', 'medley',
    'bayer', 'neoquimica', 'cimed', 'prati', 'teuto', 'hypera', 'takeda', 'astrazeneca',
    'glaxosmithkline', 'gsk', 'roche', 'merck', 'msd', 'boehringer', 'ingelheim',
    'abbott', 'libbs', 'novo', 'nordisk', 'biolab', 'farmoquimica', 'fqm', 'gross',
    'sigma', 'pharma', 'legrand', 'natulab', 'brainfarma', 'uniao', 'quimica',
    'geolab', 'greenpharma', 'multilab', 'herbarium', 'vitapan', 'zambon', 'schering',
    'plough', 'janssen', 'cilag', 'dermage', 'darrow', 'theraskin', 'nycomed',
    'abbvie', 'ferring', 'lilly', 'eli', 'servier', 'torrent', 'glenmark',
    'mg', 'g', 'ml', 'l', 'mcg', 'ui', 'unidades', 'comprimidos', 'capsulas', 'tabletes',
    'doses', '50mg', '100mg', '150mg', '200mg', '250mg', '300mg', '400mg', '500mg',
    '600mg', '750mg', '800mg', '1000mg', '1g', '2g', '5ml', '10ml', '15ml', '20ml',
    '30ml', '60ml', '100ml', '200ml', 'ug', 'microgramas', 'gramas', 'mililitros',
    'percent', 'porcento', 'vial', 'ampolas', 'frascos', 'bisnagas', 'saches',
    'envelopes', 'unidade', 'dose', 'mgml', 'uiml', 'uimg', 'kg',
    'comprimido', 'capsula', 'dragea', 'pastilha', 'solucao', 'suspensao', 'xarope',
    'gotas', 'injetavel', 'creme', 'pomada', 'gel', 'supositorio', 'efervescente',
    'oral', 'topico', 'sublingual', 'nasal', 'oftalmico', 'otologico', 'vaginal',
    'retal', 'inalatorio', 'spray', 'aerossol', 'po', 'sache', 'granulado', 'pasta',
    'emulsao', 'loção', 'colirio', 'suspensão', 'elixir', 'xampu', 'shampoo',
    'comprimidosrevestidos', 'capsulasmoles', 'capsulasduras', 'comprimidosmastigaveis',
    'comprimidosdispersiveis', 'solucoes', 'suspensoes', 'poefervescente', 'tablete',
    'tabs', 'cap', 'inj', 'viaoral', 'viatopica', 'viainjetavel', 'viainalatoria',
    'embalagem', 'caixa', 'frasco', 'ampola', 'blister', 'cartela', 'pacote', 'saco',
    'bisnaga', 'tubo', 'envase', 'rotulo', 'etiqueta', 'lacre', 'selo', 'autenticidade',
    'rastreabilidade', 'codigo', 'barras', 'qrcode', 'serial', 'identificacao', 'produto',
    'lote', 'validade', 'fabricacao', 'fab', 'exp', 'val', 'data', 'prazo', 'n', 'numero',
    'contem', 'contém', 'un', 'unid', 'fr', 'cart', 'bis', 'amp', 'sach', 'env',
    'emb', 'primaria', 'secundaria', 'terciaria', 'inviolavel', 'fecho', 'tampa',
    'rosqueavel', 'lacrado', 'protegido', 'interno', 'externo', 'folha', 'aluminio',
    'plastico', 'vidro', 'papel', 'cartonagem', 'impresso', 'colorido', 'transparente',
    'opaco', 'reciclavel', 'descartavel', 'reutilizavel', 'manuseio', 'abertura',
    'fechamento', 'dispensador', 'aplicador', 'bico', 'conta', 'gotas', 'valvula',
    'pulverizador', 'seringa', 'dosadora', 'colher', 'copo', 'medidor', 'graduado',
    'pipeta', 'adaptador', 'bula', 'instrucao', 'folheto', 'informativo', 'externo',
    'interno', 'impressao', 'texto', 'letra', 'fonte', 'tamanho', 'legivel', 'braille',
    'conservacao', 'armazenamento', 'temperatura', 'ambiente', 'refrigeracao',
    'protegido', 'luz', 'umidade', 'manter', 'fechado', 'original', 'fresco', 'seco',
    'ventilado', 'longe', 'calor', 'fontes', 'ignicao', 'congelamento', 'geladeira',
    'refrigerar', 'entre', 'graus', 'celsius', 'centigrados', 'acima', 'abaixo',
    'uso', 'adulto', 'pediatrico', 'idoso', 'gestante', 'lactante', 'crianca', 'bebe',
    'via', 'administracao', 'posologia', 'dose', 'diaria', 'unica', 'dividida',
    'intervalo', 'horario', 'manhã', 'tarde', 'noite', 'jejum', 'apos', 'refeicao',
    'antes', 'durante', 'ingerir', 'engolir', 'mastigar', 'dissolver', 'chupar',
    'aplicar', 'instilar', 'inalar', 'espirrar', 'pulverizar', 'espalhar', 'massagear',
    'fricionar', 'limpar', 'secar', 'proteger', 'curativo', 'local', 'sistemico',
    'instruções', 'modo', 'usar', 'agitar', 'antes', 'homogeneizar', 'suspender',
    'reconstituir', 'diluir', 'agua', 'liquido', 'soluvel', 'dispersivel', 'mastigavel',
    'sublingual', 'topico', 'externo', 'interno', 'superficial', 'profundo', 'anos',
    'composicao', 'componente', 'excipiente', 'inativo', 'contem', 'contém', 'lactose',
    'gluten', 'acucar', 'corante', 'conservante', 'aromatizante', 'edulcorante',
    'estabilizante', 'veiculo', 'solvente', 'diluente', 'emulsificante', 'espessante',
    'antioxidante', 'quelante', 'regulador', 'ph', 'isotonico', 'estéril', 'pirogenio',
    'livre', 'sem', 'adicao', 'natural', 'artificial', 'sintetico', 'derivado',
    'alta', 'concentracao',
    'venda', 'receita', 'controlado', 'tarja', 'vermelha', 'preta', 'branca', 'livre',
    'prescricao', 'medica', 'farmacia', 'drogaria', 'anvisa', 'registro', 'ms', 'cnpj',
    'industria', 'farmaceutica', 'laboratorio', 'distribuido', 'importado', 'fabricado',
    'produzido', 'comercializado', 'autorizado', 'notificado', 'isento', 'dispensacao',
    'restrita', 'especial', 'lei', 'regulamentacao', 'vigilancia', 'sanitaria',
    'sodica', 'cloridrato', 'diidratado', 'base', 'acido', 'fosfato',
    'sulfato', 'maleato', 'citrato', 'succinato', 'propionato', 'associado', 'composto',
    'complexo', 'prolongado', 'retard', 'liberacao', 'controlada', 'imediata', 'rapida',
    'sustentada', 'modificada', 'encapsulado', 'micronizado', 'cristalino', 'amorfo',
    'estere', 'sal', 'hidrato', 'anidro', 'polimorfo', 'enantiomero', 'racemico', 'antigases', 'rapido',
    'cuidado', 'advertencia', 'precaucao', 'perigo', 'restricao', 'proibido', 'nao',
    'ingerir', 'aplicar', 'inalar', 'exceder', 'dose', 'recomendada', 'manter', 'fora',
    'alcance', 'criancas', 'pets', 'animais', 'evitar', 'contato', 'olhos', 'mucosas',
    'pele', 'lesionada', 'irritada', 'suspender', 'uso', 'caso', 'reacao', 'adversa',
    'alergica', 'consultar', 'medico', 'farmaceutico', 'urgencia', 'emergencia',
    'intoxicacao', 'superdose', 'acidental', 'orientacao', 'profissional', 'saude',
    'gravidez', 'amamentacao', 'lactacao', 'condicao', 'medica', 'preexistente',
    'alergia', 'hipersensibilidade', 'contraindicacao', 'interacao', 'medicamentosa',
    'alcool', 'bebida', 'alcolica', 'dirigir', 'operar', 'maquinas', 'equipamentos',
    'medicamento',
    'e', 'de', 'para', 'com', 'em', 'no', 'na', 'a', 'o', 'as', 'os', 'um', 'uma',
    'sob', 'acima', 'abaixo', 'antes', 'depois', 'durante', 'ate', 'entre', 'por',
    'cada', 'vez', 'vezes', 'ao', 'dia', 'semana', 'mes', 'ano', 'inicio', 'fim',
    'contem:', 'no', 'acao', 'alivio', 'dos', 'sintomas', 'horas', 'diario', 'mensal',
    'semanal', 'continuo', 'intermitente', 'indicado', 'tratamento', 'prevencao',
    'diagnostico', 'sintomatico', 'terapeutico', 'novo', 'melhorado', 'avancado',
    'exclusivo', 'original', 'similar', 'generico', 'referencia', 'b', 'r', 'g',
    'nº', 'lei', 'alergica', 'contato', 'informacoes', 'adicional', 'consulte',
    'endereco', 'telefone', 'sac', 'atendimento', 'consumidor', 'site', 'website',
    'online', 'lancamento', 'promocao', 'oferta', 'desconto', 'brinde', 'amostra',
    'gratis', 'limitada', 'estoque', 'disponibilidade', 'mercado', 'nacional',
    'internacional', 'importacao', 'exportacao', 'distribuicao', 'logistica', 'causados', 'pelos',
    'rinite', 'urticaria', 'alergia', 'alergias', 'dor', 'febre', 'inflamacao',
    'infeccao', 'tosse', 'gripe', 'resfriado', 'congestao', 'nasal', 'sinusite',
    'bronquite', 'asma', 'enxaqueca', 'cefaleia', 'dor de cabeça', 'colica',
    'diarreia', 'constipacao', 'nausea', 'vomito', 'gastrite', 'refluxo', 'azia',
    'indigestao', 'flatulencia', 'hemorroidas', 'insonia', 'ansiedade', 'depressao',
    'estresse', 'hipertensao', 'hipotensao', 'arritmia', 'colesterol', 'diabetes',
    'hipoglicemia', 'hiperglicemia', 'artrite', 'artrose', 'reumatismo', 'gota',
    'lombalgia', 'dor muscular', 'dor articular', 'tendinite', 'bursite', 'cramps',
    'espasmo', 'convulsao', 'epilepsia', 'vertigem', 'tontura', 'labirintite',
    'otite', 'conjuntivite', 'blefarite', 'glaucoma', 'catarata', 'irritacao',
    'ocular', 'dermatite', 'eczema', 'psoriase', 'acne', 'micose', 'herpes',
    'verruga', 'coceira', 'prurido', 'edema', 'inchaço', 'hematoma', 'ferida',
    'corte', 'queimadura', 'ulceras', 'varizes', 'trombose', 'anemia', 'imunidade',
    'deficiencia', 'vitaminica', 'fadiga', 'cansaco', 'fraqueza', 'osteoporose',
    'menopausa', 'tpm', 'candidiase', 'infecao urinaria', 'prostatite', 'impotencia',
    'disfuncao', 'erétil', 'fertilidade', 'gravidez', 'lactacao', 'amamentacao',
    'sintomas', 'alívio', 'tratamento', 'prevencao', 'controle', 'melhora',
    'reducao', 'combate', 'protecao', 'cura', 'bemestar', 'saude', 'conforto',
    'recuperacao', 'regeneracao', 'hidratacao', 'nutricao', 'fortalecimento',
    'equilibrio', 'estabilidade', 'funcionamento', 'normal', 'regular', 'diario',
    'natural', 'organico', 'clinico', 'agudo', 'cronico', 'leve', 'moderado', 'grave',
    'abdominal', 'estufamento', 'desconforto', 'gases'
}

base_medications = [
    'dipirona monoidratada', 'dipirona', 'paracetamol', 'dicloridrato de levocetirizina',
    'ibuprofeno', 'domperidona', 'acebrofilina'
]

# Cache de tokenização para medicamentos base
tokenized_medications = {
    med: nltk.tokenize.word_tokenize(med, language="portuguese")
    for med in base_medications
}

def removeStopWords(words):
    """Remove palavras da lista de stopwords."""
    return [word for word in words if word not in stopwords]

def compareText(text):
    """Compara texto filtrado com medicamentos base usando similaridade de Jaccard."""
    tokensText = text.split()
    textSize = len(tokensText)

    for medicine, tokensMedicine in tokenized_medications.items():
        medicineSize = len(tokensMedicine)
        interseccao = sum(1 for token in tokensText if token in tokensMedicine)
        union = textSize + medicineSize - interseccao
        jaccard = interseccao / union if union != 0 else 0

        if jaccard > 0.3:
            return medicine
    return ""

def process_text(text):
    """Pré-processa o texto e compara com medicamentos."""
    if not text:
        return "", ""
    
    text = unidecode(text.lower())
    text = re.sub(r'[^\w\s]|\d+', '', text)
    words = text.split()
    filtered_words = removeStopWords(words)
    filtered_text = ' '.join(filtered_words)
    matched_medication = compareText(filtered_text)
    return text, matched_medication