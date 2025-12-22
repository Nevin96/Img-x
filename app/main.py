from fastapi import FastAPI

app = FastAPI(title = 'Imgx - Image Processing API')

@app.get('/')
def status_check():
    return 'imagex is running'
