from pathlib import Path
from rich.console import Console
import subprocess

console=Console()


class Project:
    def create(self, name:str, git:bool=True):
        project_path =Path(name)

        if project_path.exists():
            console.print("[red]Error:[/red]Projects already exists")
            return
        #structure
        project_path.mkdir()
        (project_path / 'src').mkdir()
        (project_path / 'README.md').touch() # touch() creaes and empty file

        #git intialiazation

        if git:
            subprocess.run(
                ['git','init', str(project_path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            console.print("Git Initialized")
        
            console.print('[bold green] Project Created Successfully [/bold green]')
            console.print(f'{project_path}/')
            