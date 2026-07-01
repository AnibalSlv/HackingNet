from textual.widgets import *
from engine.core import Core

class RenderProfile(TabPane):
    def __init__(self, player) -> None:
        super().__init__("Perfil", id="profile")
        self.player = player
    
    def compose(self):
        yield Static("[bold green]Este es tu perfil[/]")
        yield Static("[bold green]=========================[/]")
        yield Static(f"[green]Nombre: {self.player.name}[/]")
        yield Static(f"[green]Dinero: {self.player.money}[/]")
        yield Static(f"[green]Prestigio: {self.player.prestige}[/]")
        yield Static(f"[green]Herramientas: {self.player.tools}[/]")
        yield Static(f"[green]Red Actual: {self.player.ip_current}[/]")
        yield Static("[bold green]=========================[/]")

        yield Input(placeholder="", id="buscador_pestanas")
