from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="User Data")

table.add_column("ID", style="blue", no_wrap=True)
table.add_column("Name", style="purple")
table.add_column("Age", style="yellow")

table.add_row("1", "Alice", "20")
table.add_row("2", "Bob", "30")
table.add_row("3", "Charlie", "40")

console.print(table)