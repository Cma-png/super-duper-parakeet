# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install additional system dependencies for running PyTorch and Stable Diffusion
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /app

# Set the environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLE_CORS=False
ENV STREAMLIT_SERVER_HEADLESS=True

# Expose port 8501 for Streamlit
EXPOSE 8501

# Command to run the streamlit app
CMD ["streamlit", "run", "app.py"]