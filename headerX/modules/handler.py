import asyncio
import sys
import argparse
from rich.console import Console
from rich.panel import Panel

from .helper import print_banner, show_help
from .header_analyzer import HeaderAnalyzer

console = Console()

def main_handler():

    if "-h" in sys.argv or "--help" in sys.argv:
        print_banner()
        show_help()
        sys.exit()

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("url", help="Target domain or full URL")
    args = parser.parse_args()

    asyncio.run(run_analysis(args.url))

async def run_analysis(url: str):
    analyzer = HeaderAnalyzer()
    with console.status(f"[bold bright_cyan]Fetching headers from[/] {url}...", spinner="aesthetic", spinner_style="bold bright_green"):
        try:
            raw_req, raw_res = await analyzer.fetch_headers(url)
        except RuntimeError as e:
            console.print(f"[bold bright_red]Error:[/] {e}")
            return

    console.print(Panel(
        analyzer.highlight_headers(raw_req),
        title="[bold]Request Headers[/]", 
        title_align="left", 
        border_style="bold bright_cyan", 
        expand=False
    ))

    console.print(Panel(
        analyzer.highlight_headers(raw_res, is_response=True),
        title="[bold]Response Headers[/]", 
        title_align="left", 
        border_style="bold bright_magenta", 
        expand=False
    ))

    