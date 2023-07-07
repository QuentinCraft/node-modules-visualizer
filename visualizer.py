import sys
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep

from scan import Scan

PATH = sys.argv[1] if len(sys.argv) > 1 else "." # Get the path from the command line arguments
CONSOLE = Console() # Create a console

scanner = Scan(PATH) # Scan the current directory

scanner.scan(target="node_modules", console=CONSOLE) # Scan the directory

table = Table(title="Node Visualizer") # Create a table with a title

table.add_column("Project Name", justify="center", style="cyan")
table.add_column("Path", justify="center", style="magenta")
table.add_column("Size", justify="center", style="green")

for result in scanner.results:
    table.add_row(result[0], result[1], result[2]) # Add a row to the table

CONSOLE.print(table, justify="center") # Print the tables

CONSOLE.print(f"Possible reclaimed size on disk 💾 : [bold green]{scanner.convert_size(scanner.size)}", justify="center") # Print a message
CONSOLE.print(f"Total node_modules folders 📁 : [bold green]{scanner.folders}", justify="center") # Print a message
