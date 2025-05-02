from pymongo import MongoClient
from Youtube.config import Config

client = MongoClient(Config.MONGO_URL)
db = client['ytbot']
thumbs = db['thumbnails']

def save_thumbnail(user_id: int, file_id: str):
    thumbs.update_one({"user_id": user_id}, {"$set": {"file_id": file_id}}, upsert=True)

def get_thumbnail(user_id: int):
    data = thumbs.find_one({"user_id": user_id})
    return data['file_id'] if data else None

def delete_thumbnail(user_id: int):
    thumbs.delete_one({"user_id": user_id})
