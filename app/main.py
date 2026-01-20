from fastapi import FastAPI
from app.core.config import settings
from app.auth.routes import router as auth_router

app = FastAPI(title = 'Imgx - Image Processing API',version='0.1.0')
app.include_router(auth_router)
@app.get("/")
def status_check():
    return {'status' : 'running',
            'project' : settings.PROJECT_NAME}
