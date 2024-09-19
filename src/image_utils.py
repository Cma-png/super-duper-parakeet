from PIL import Image
import io
from src.logger import logger

def save_image(image, file_path):
    """Save the generated image to a specified file path."""
    try:
        image.save(file_path)
        logger.info(f"Image saved successfully at: {file_path}")
    except Exception as e:
        logger.error(f"Error saving image: {e}")
        raise

def get_image_bytes(image):
    """Converts an image into byte stream for download purposes."""
    try:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        logger.info("Image converted to byte stream successfully")
        return img_byte_arr
    except Exception as e:
        logger.error(f"Error converting image to byte stream: {e}")
        raise