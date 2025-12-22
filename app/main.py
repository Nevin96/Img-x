from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title = 'Imgx - Image Processing API',version='0.1.0')

@app.get("/")
def status_check():
    return {'status' : 'running',
            'project' : settings.PROJECT_NAME}
