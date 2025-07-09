import os
from box.exceptions import BoxValueError #exceptional handling
import yaml
from cnnClassfier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
        ValueError: if yaml file is empty
        e:empty file
    Returns:
        ConfigBox: ConfigBox type"""
    try:
        with open(path_to_yaml) as yaml_files:
            content = yaml.safe_load(yaml_files)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ craete list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"craeted directory at:{path}")

@ensure_annotations
def save_json(path: Path, data:dict):
    """ save json data
    Args:
        path (Path): path to json file
        data(dict): data to be saved in json file"""
    with open(path, "w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """ load json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attribute instead of dict"""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path: Path):
    """ save binary files
    Args:
        data(Any): data to be saved as binary
        path (Path): path to binary file
        """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """ load binary data
    Args:
        path (Path): path to bainary file
    Returns:
        Any: object stored in the file"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """ get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def decodeImage(impstring,filename):
    imgdata = base64.b64decode(impstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
@ensure_annotations
def encodeImage(crappedimagepath):
    with open(crappedimagepath, 'rb') as f:
        return base64.b64encode(f.read())