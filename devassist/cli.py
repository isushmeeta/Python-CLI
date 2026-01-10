import fire 

from rich.console import Console

from devassist.project import project

console = Console()

class DevAssist:


    def init(self, name:str):

        console.print(f"[green] Initilaizing project : [/green] {name}")

