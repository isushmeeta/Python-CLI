import fire 

from rich.console import Console

from devassist.project import project

console = Console()

class DevAssist:


    def init(self, name:str):

        console.print(f"[green] Initilaizing project : [/green] {name}")
        Project().create(name)

def main():
    fire.Fire(DevAssist)

if __name__== "__main__":
    main()
