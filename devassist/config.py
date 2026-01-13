import yaml
from pathlib import Path
from rich.console import Console

console=Console()
CONFIG_DIR = Path.home() 
CONFIG_FILE=CONFIG_DIR 

#load config
def load_config():
    if not CONFIG_FILE.exists():
        return{}
    with open(CONFIG_FILE,"r") as f:
        return yaml.safe_load(f) or {} #emty yaml file returns None so used  { } to prevent crashes

#save config file
def save_config(config: dict):

    CONFIG_DIR.mkdir(exist_ok=True) #Prevents crash if folder already exists

    with open(CONFIG_FILE,"w") as f:
        yaml.safe_dump(config, f)