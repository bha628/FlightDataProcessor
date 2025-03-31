import logging

# Logging configuration
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "flight_data_processor.log"

# Flight status options
FLIGHT_STATUSES = {"ON_TIME", "DELAYED", "CANCELLED"}

# Default settings
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M"