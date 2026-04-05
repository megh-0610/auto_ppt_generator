from fastapi import FastAPI
from image_services import download_image

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server running"}

@app.get("/generate-ppt")
def generate(topic: str):
    file_path = run(topic)
    return {"ppt_file": file_path}