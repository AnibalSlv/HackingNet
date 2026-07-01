from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, TabbedContent, TabPane, Static
from render.render_red import RenderRed
from render.render_profile import RenderProfile
from render.game.render_game import RenderGame

from commands.global_commands import command_global

from engine.core import Core

class AppNavegacionPorTexto(App):
    # Añadimos un poco de margen para que la interfaz respire visualmente
    CSS = """
    TabbedContent ContentTabs {
        display: none;
    }
    Input {
        margin: 1 2;
    }
    TabbedContent {
        margin: 1 2;
    }
    """

    def __init__(self):
        super().__init__()
        self.game = Core()
        

    def compose(self) -> ComposeResult:
        yield Header()
                
        # El contenedor de pestañas con sus IDs definidos
        #! INITIAL ABRE POR DEFECTO LA PESTANA CON ESA ID
        with TabbedContent(initial="profile", id="windows"):
            yield RenderRed()
            yield RenderProfile(self.game.player)
            yield RenderGame()
                
        yield Footer()

    # Evento que se dispara al presionar Enter en el Input
    def on_input_submitted(self, event: Input.Submitted) -> None:

        inputUser = event.value.strip().lower().split()

        # 2. Obtenemos el widget de las pestañas
        tabbed_content = self.query_one("#windows", TabbedContent)
        
        # 3. Definimos cuáles son los IDs válidos para evitar errores
        pestanas_disponibles = ["red", "profile"]

        command = inputUser[0]

        if command in command_global:
            if command == "cd":
                if len(inputUser) < 2:
                    self.notify("Debes especificar un destino. Ejemplo: cd perfil", severity="error")
                    return
                
                destination = inputUser[1]
                
                if destination not in pestanas_disponibles:
                    self.notify(
                        f"Destino '{destination}' no válido. Prueba con el comando ls para ver los directorios.", 
                        severity="warning"
                    )
                else:
                    tabbed_content.active = destination

            else:
                execute_command = command_global[command]
                execute_command(self)

        # 4. Limpiamos el input para que pueda volver a escribir cómodamente
        event.input.value = ""

if __name__ == "__main__":
    app = AppNavegacionPorTexto()
    app.run()