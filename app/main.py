from fastapi import FastAPI
from app.core.config import settings
from app.auth.routes import router as auth_router
from app.images.routes import router as image_router
from app.images.transform_routes import router as transform_router
from app.images.dynaminc_routes import router as dynamic_router
from fastapi.staticfiles import StaticFiles


app = FastAPI(title = 'Imgx - Image Processing API',version='0.1.0')
app.include_router(auth_router)
app.include_router(image_router)
app.include_router(transform_router)
app.include_router(dynamic_router)
app.mount("/media",StaticFiles(directory='media'),name='media')
@app.get("/")
def status_check():
    return {'status' : 'running',
            'project' : settings.PROJECT_NAME}
