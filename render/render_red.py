from textual.widgets import *
from render.game.render_game import RenderGame



avalible_red = ["192.168.1.15"]

class RenderRed(TabPane):
    def __init__(self) -> None:
        super().__init__("Red", id="red")
    
    def compose(self):

        yield Static("Bienvenido a la Red *Emoji calavera*")

        for red in avalible_red:
            yield Static(f"[yellow]{red}[/]: Demo")

        yield Input(placeholder="", id="buscador_pestanas")
        
    def on_input_submitted(self, event: Input.Submitted):
        inputUser = event.value.strip().lower().split()
        
        command = inputUser[0]

        if command in "command_red":
            if len(inputUser) < 2:
                self.notify("Debes especificar una red. Ejemplo: cat 123.456.7.8", severity="error")
                return

            target_ip = inputUser[1]

            tabbed_content = self.app.query_one("#windows", TabbedContent)
            render_game = self.app.query_one("#game")
            render_game.updateValueIp(target_ip) 
            tabbed_content.active = "game"