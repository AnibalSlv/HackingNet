from textual.widgets import *
from engine.core import Core

# aja ve esto, lo que enviamos al main es esta clase
# esta clase contiene el metodo compose(self)
# esto es lo que le permite a textual renderizar elementos
class RenderProfile(TabPane):
    def __init__(self, player) -> None:
        super().__init__("Perfil", id="profile")
        self.player = player
    
    def compose(self):
        # cuando llamamos desde el main al RenderProfile lo que estamos llamado es a todo este archivo
        # y como el archivo tiene el metodo compose y el yield nos permite mostrar elementos 
        # yield sabe que tiene que mostrar todo lo que este dentro de compose 
        # me explique  xd ? 
        #pos si ya le entendi mejor blo 

        #ok vamos al main de nuevo

        yield Static("[bold green]Este es tu perfil[/]")
        yield Static("[bold green]=========================[/]")
        yield Static(f"[green]Nombre: {self.player.name}[/]")
        yield Static(f"[green]Dinero: {self.player.money}[/]")
        yield Static(f"[green]Prestigio: {self.player.prestige}[/]")
        yield Static(f"[green]Herramientas: {self.player.tools}[/]")
        yield Static(f"[green]Red Actual: {self.player.ip_current}[/]")
        yield Static("[bold green]=========================[/]")

        yield Input(placeholder="", id="buscador_pestanas")
