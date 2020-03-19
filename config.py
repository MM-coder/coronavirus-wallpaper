import sys
import os
 
data = {"country": "World"}

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.normpath(os.path.join(base_path, relative_path))
    
data = {"country": "World"}

def load_option_from_config(op: str):
    return data[op]

def write_option_to_config(op: str, value: str):
    data[op] = value
    return data