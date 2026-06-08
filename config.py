import os

class Config:
    SECRET_KEY = "talent-track-secret"
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    ALLOWED_EXTENSIONS = {"txt"}
