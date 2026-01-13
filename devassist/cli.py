#cli-entry the user interaction part
import fire 
from rich.console import Console
from devassist.config import load_config
from devassist.project import Project


console = Console()

class DevAssist:
    def init(self, name:str,git:bool=None):
        config=load_config
        if git is None:
            git =config.get("default.git", True)
        console.print(f"[green]Initializing project:[/green] {name}")
        Project().create(name,git)

    

    def config(self, action:str, key:str =None, value:str =None): # fire will convert this entire function to "devassist init name"
        config =load_config()
        if action == "'set":
            if key is None or value is None:
                console.print("[red]Error:[/red] Key and value required")
                return 
            config[key]=value
            save_config(config)
            console.print(f"[green]Config set:[/green] {key} = {value}")

        elif action =="get":

            if key is None:
                console.print("[red]Error:[/red] Key required")
                return
            value=config.get(key)
            if value is None:
                console.print("[yellow]Not set[/yellow]")
            else:
                console.print(f"[cyan] {key}[/cyan]={value}")
        else:
            console.print("[red]Unknown action[/red]")
            

        
        

def main():
    fire.Fire(DevAssist) #this alone will read the above class, generate commands and maps CLI args to Pyhton args

if __name__== "__main__":
    main()
