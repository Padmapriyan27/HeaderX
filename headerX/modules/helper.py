from rich.console import Console
from rich.panel import Panel

console = Console()

def print_banner() -> None:
    bannner = """
 █████                             █████                    █████ █████
░░███                             ░░███                    ░░███ ░░███ 
 ░███████    ██████   ██████    ███████   ██████  ████████  ░░███ ███  
 ░███░░███  ███░░███ ░░░░░███  ███░░███  ███░░███░░███░░███  ░░█████   
 ░███ ░███ ░███████   ███████ ░███ ░███ ░███████  ░███ ░░░    ███░███  
 ░███ ░███ ░███░░░   ███░░███ ░███ ░███ ░███░░░   ░███       ███ ░░███ 
 ████ █████░░██████ ░░████████░░████████░░██████  █████     █████ █████
░░░░ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░     ░░░░░ ░░░░░ 
"""
    console.print(bannner, style="bold bright_green")


def show_help():
    help_text = """
[bold bright_cyan]HTTP Header Analyzer[/]

[bold orange_red1]Beta version 0.2[/]

[bold bright_yellow]Usage:[/] python -m headerX.headerX [cyan]url[/]

[bold green]Positional Arguments:[/]
  [bright_cyan]url[/]          Target domain or full URL (e.g., https://example.com)

[bold green]Optional Arguments:[/]
  [bright_cyan]-h, --help[/]    Show this help message

[bold]Example:[/]
  [bright_green]python -m headerX.headerX https://example.com[/]
"""
    console.print(Panel(help_text, title="Help",title_align="left", border_style="bold orange_red1", expand=False))