import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from src.logger import logger

class DiffusionPipeline:
    def __init__(self, model_id="stabilityai/stable-diffusion-2"):
        logger.info(f"Initializing diffusion pipeline with model: {model_id}")
        try:
            self.model_id = model_id
            self.scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
            self.pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=self.scheduler, torch_dtype=torch.float16)
            
            # Choose device (CUDA if available)
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.pipe.to(self.device)
            logger.info(f"Model loaded successfully on device: {self.device}")
        except Exception as e:
            logger.error(f"Error during model initialization: {e}")
            raise

    def generate_image(self, prompt):
        """Generates an image from the given prompt using the Stable Diffusion model."""
        logger.info(f"Generating image for prompt: {prompt}")
        try:
            image = self.pipe(prompt).images[0]
            logger.info(f"Image generation successful for prompt: {prompt}")
            return image
        except Exception as e:
            logger.error(f"Error generating image: {e}")
            raise