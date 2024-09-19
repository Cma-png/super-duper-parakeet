import streamlit as st
from src.diffusion_pipeline import DiffusionPipeline
from src.image_utils import get_image_bytes
from src.logger import logger

# Initialize the diffusion pipeline
pipeline = DiffusionPipeline()

# Title and input section
st.title("Local Image Generation with Stable Diffusion")
prompt = st.text_input("Enter your prompt:", "A beautiful landscape")

# Placeholder for the generated image
image = None

# Generate the image when button is clicked
if st.button("Generate Image"):
    logger.info(f"User submitted prompt: {prompt}")
    with st.spinner("Generating image..."):
        try:
            image = pipeline.generate_image(prompt)
            st.image(image, caption="Generated Image", use_column_width=True)
            logger.info("Image successfully displayed")
        except Exception as e:
            st.error(f"Failed to generate image: {e}")
            logger.error(f"Image generation failed for prompt: {prompt} with error: {e}")

# Option to download the generated image if it exists
if image:
    image_bytes = get_image_bytes(image)
    st.download_button(label="Download Image", data=image_bytes, file_name="generated_image.png")
    logger.info(f"Image available for download")