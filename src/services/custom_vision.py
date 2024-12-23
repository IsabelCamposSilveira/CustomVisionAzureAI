from utils.Config import Config
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

def custom_vision(blob_url):
    # Configurações do Custom Vision
    TAG_NAME = "Frio"  # Nome da tag que você deseja associar à imagem

    # Autenticação
    credentials = ApiKeyCredentials(in_headers={"Training-key": Config.TRAINING_KEY})
    trainer = CustomVisionTrainingClient(Config.ENDPOINT, credentials)

    # URL da imagem no Blob Storage
    image_url = blob_url 

    # Obtém a tag associada ao projeto
    tags = trainer.get_tags(Config.PROJECT_ID)
    tag_id = next((tag.id for tag in tags if tag.name == TAG_NAME), None)

    if not tag_id:
        return "Erro na TAG"
    
    # Adiciona a imagem ao projeto usando a URL
    try:
        batch = {
            "images": [
                {
                    "url": image_url,
                    "tagIds": [tag_id],
                }
            ]
        }
        result = trainer.create_images_from_urls(Config.PROJECT_ID, batch)
        return f"Imagem enviada com sucesso! \n {result.is_batch_successful}"
    except Exception as e:
        return e
