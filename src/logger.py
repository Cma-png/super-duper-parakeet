import logging
import os

def setup_logger():
    """Sets up the logger to log info, debug, and error messages."""
    log_dir = "logs"
    log_file = os.path.join(log_dir, "app.log")
    
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Logs to console
        ]
    )
    
    logger = logging.getLogger(__name__)
    return logger

logger = setup_logger()