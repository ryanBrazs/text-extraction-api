import os
import json
from google.oauth2 import service_account
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env, se presente
load_dotenv()

# Configura as credenciais do Google Cloud a partir da variável de ambiente
GOOGLE_CREDENTIALS_JSON = os.environ.get('GOOGLE_CREDENTIALS_JSON')
if not GOOGLE_CREDENTIALS_JSON:
    raise ValueError("A variável de ambiente GOOGLE_CREDENTIALS_JSON não está definida.")

credentials = service_account.Credentials.from_service_account_info(
    json.loads(GOOGLE_CREDENTIALS_JSON),
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)