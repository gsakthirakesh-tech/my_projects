import os

from dotenv import load_dotenv

load_dotenv()

url = os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_API_KEY")
collection_name = os.getenv("COLLECTION_NAME", "my_collection")
model = os.getenv("MODEL", "all-MiniLM-L6-v2")