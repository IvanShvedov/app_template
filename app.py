import logging
import os

from config import Config
from constants import LOG_DIR, CONFIG_FILE_PATH

# Config init
config = Config(yaml_file=CONFIG_FILE_PATH)

# Logger init
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set log handler
fh = logging.FileHandler(f"{LOG_DIR}/all.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Init app