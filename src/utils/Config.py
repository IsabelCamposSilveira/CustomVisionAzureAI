import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBSCRIPTION_KEY")
    AZURE_STOREGE_CONNECTION_STRING = os.getenv("AZURE_STOREGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")  
    TRAINING_KEY =  os.getenv("TRAINING_KEY")  
    PROJECT_ID = os.getenv("PROJECT_ID")  