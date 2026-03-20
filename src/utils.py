import logging
import os


# -----------------------------------------------------------
# Setup logging configuration for the pipeline
# -----------------------------------------------------------

def setup_logging():
    """
    Configure logging for the project.

    - Creates logs directory if it does not exist
    - Logs messages to a file
    - Uses a consistent format with timestamp and level

    Returns:
        logger instance
    """

    # ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # configure logging settings
    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    # return logger for use in other modules
    return logging.getLogger(__name__)