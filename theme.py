from rich.console import Console
from rich.theme import Theme

console = Console(theme=Theme({
    "heading": "rgb(175,0,255)",
    "border": "dim cyan",
    "X": "bold magenta",
    "O": "blue",
    "draw": "dim red",
    "success": "bold green",
    "lost": "red"
}))
