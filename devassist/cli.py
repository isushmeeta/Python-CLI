#cli-entry the user interaction part
import fire 

from rich.console import Console

from devassist.project import project

console = Console()

class DevAssist:
    def init(self, name:str): # fire will convert this entire function to "devassist init name"

        console.print(f"[green] Initilaizing project : [/green] {name}")
        Project().create(name)

def main():
    fire.Fire(DevAssist) #this alone will read the above class, generate commands and maps CLI args to Pyhton args

if __name__== "__main__":
    main()
