import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #how the log is stored --> information level

log_dir = "logs" #a log folder is created
log_filepath = os.path.join(log_dir,"running_logs.log") #inside the log folder a log file is created
os.makedirs(log_dir,exist_ok=True)  

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [  #i need the logs in file as well as terminal
      logging.FileHandler(log_filepath),
      logging.StreamHandler(sys.stdout)  
    ]
)

logger = logging.getLogger("cnnClassifierLogger") #logger object