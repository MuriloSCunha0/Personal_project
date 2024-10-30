from googleapiclient.discovery import build
from google.oauth2 import service_account

# Configurar o serviço do Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def get_video_url_from_drive(exercise_name):
    """Busca o arquivo no Google Drive pelo nome do exercício e retorna o link compartilhável."""
    query = f"name = '{exercise_name}' and mimeType = 'video/mp4'"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        return None  # Não encontrou o vídeo

    # Retornar o link do vídeo
    video_id = items[0]['id']
    return f"https://drive.google.com/file/d/{video_id}/view?usp=sharing"


