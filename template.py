import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = 'cnnClassfier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #to make filepath run in every system
    filedir, filename = os.path.split(filepath) #seperating folder and files
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #create folder if it exits it won't or else it creates
        logging.info(f"Creating Directory; {filedir} fo the file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0): #if the file doesn't exit or the size of file is zero
        with open(filepath, "w") as f: #creating file
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")