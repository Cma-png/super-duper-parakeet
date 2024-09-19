# Local Image Generation with Diffusion Models

This project allows users to generate images interactively based on text prompts using a Stable Diffusion model. The model is powered by Hugging Face's `diffusers` library and runs in a local environment.

## Prerequisites

Before you run this project, make sure to have the following installed:

- Python 3.10+
- Virtual environment (e.g., `venv`)
- Hugging Face account
- Access to the Stable Diffusion model from Hugging Face

## Setup

1. **Clone the repository:**

   ```bash
   git clone this repository
   cd to the folder
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Login to Hugging Face:**

   This project uses the Stable Diffusion model from Hugging Face. You must log in to Hugging Face CLI with your access token before running the project.

   - Apply for access to the Stable Diffusion 2.1 model at [Hugging Face's model page](https://huggingface.co/stabilityai/stable-diffusion-2-1).
   - After gaining access, log in to Hugging Face from the terminal:

   ```bash
   huggingface-cli login
   ```

   This will prompt you to enter your access token, which you can find on your Hugging Face account page.

5. **Run the Streamlit App:**

   After logging in, you can start the Streamlit app by running the following command:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a prompt in the text box.
2. Click the "Generate Image" button to create a new image based on your prompt.
3. You can download the generated image by clicking the "Download Image" button.

## Logs

All runtime logs are saved in the `logs/` directory. They include information about model loading, image generation, and any errors encountered during runtime.

---

This will ensure users know to log in via the CLI before running your project.
