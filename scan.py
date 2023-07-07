import os
import time

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

class Scan:
    def __init__(self, path="."):
        self.path = path
        self.size = 0
        self.files = 0
        self.folders = 0
        self.results = []
    
    def convert_size(self, size_in_bytes):
        units = ["B", "KB", "MB", "GB", "TB"]
        unit_index = 0

        while size_in_bytes >= 1024 and unit_index < len(units) - 1:
            size_in_bytes /= 1024
            unit_index += 1

        return f"{size_in_bytes:.2f} {units[unit_index]}"
    
    def scan(self, target="", console=None):
        console.print(f"[bold green]Indexing files/folders {self.path} for {target}...[/bold green]")
        directories = list(os.walk(self.path))
        with Progress() as progress:
            task = progress.add_task("[cyan]Scanning directories...", total=len(directories), console=console)

            for root, dirs, files in directories:
                for dir in dirs:
                    if dir == target:
                        dir_path = os.path.join(root, dir)
                        dir_size = os.path.getsize(dir_path)
                        converted_size = self.convert_size(dir_size)

                        self.results.append((root, dir_path, converted_size))
                        self.size += dir_size
                        self.folders += 1
                        continue
                time.sleep(0.00001)
                progress.advance(task)  # Update the progress bar

        return self
    
    def get_size(self):
        return self.size
    
    def get_files(self):
        return self.files
    
    def get_folders(self):
        return self.folders
    
    def get_results(self):
        return self.results
    
    def get_path(self):
        return self.path