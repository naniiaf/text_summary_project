import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO,format='[%(asctime)s]:%(message)s:')

profect_name="textsummeriser"

list_of_files = [
    ".github/workflows/.gitkeep",
    f'scr/{profect_name}/__inIt__.py'
    f'scr/{profect_name}/components/__inIt__.py',
    f'scr/{profect_name}/utils/__intit__.py',
    f'scr/{profect_name}/utils/common.py',
    f'scr/{profect_name}/logging/__init__.py',
    f'scr/{profect_name}/config/__init__.py',
    f'scr/{profect_name}/config/config.py',
    f'scr/{profect_name}/pipeline/__init__.py',
    f'scr/{profect_name}/entity/__init__.py',
    f'scr/{profect_name}/constants/__init__.py',
    "cconfig/config.yaml",
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'     
      
    
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory:{filedir}for file{filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating emppty file:{filename}')
            
    else:
        logging.info(f'{filename} already exists')
            