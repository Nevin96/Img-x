import os
from PIL import Image as PILImage

VARIANT_DIR = "media/variants"

os.makedirs(VARIANT_DIR,exist_ok=True)

def resize_image(input_path : str,output_path: str,width : int ,height : int):
    with PILImage.open(input_path) as img:
        resized = img.resize((width,height))
        resized.save(output_path)

def create_thumbnail(input_path : str,output_path:str,size = (200,200)):
    with PILImage.open(input_path) as img:
        img.thumbnail(size)
        img.save(output_path)

def convert_format(input_path : str,output_path : str,format : str):
    with PILImage.open(input_path) as img:
        rgb = img.convert("RGB")
        rgb.save(output_path,format=format.upper())
