from textual.app import App, ComposeResult
from textual.widgets import Input, TabbedContent

from commands.terminal import Terminal
from engine.core import Core
from render.game.render_game import RenderGame
from render.render_profile import RenderProfile
from render.render_red import RenderRed


class AppNavegacionPorTexto(App):
    # Añadimos un poco de margen para que la interfaz respire visualmente
    CSS = """
    TabbedContent ContentTabs {
        display: none;
    }
    """

    def __init__(self):
        super().__init__()
        self.game = Core()
        self.terminal = Terminal()

    def compose(self) -> ComposeResult:
        # El contenedor de pestañas con sus IDs definidos
        #! INITIAL ABRE POR DEFECTO LA PESTANA CON ESA ID
        with TabbedContent(initial="profile", id="windows"):
            yield RenderRed()
            yield RenderProfile(self.game.player)
            yield RenderGame()

    # Evento que se dispara al presionar Enter en el Input
    def on_input_submitted(self, event: Input.Submitted) -> None:
        texto_usuario = event.value
        result = self.terminal.execute(texto_usuario)
        event.input.value = ""

        if not result:
            return

        # Manejo visual de errores y mensajes
        if result.error:
            self.notify(result.output, severity="error")
        else:
            self.notify(result.output)

        # Manejo de cambio de pantalla
        tabbed_content = self.query_one("#windows", TabbedContent)

        # Cambia de ventana
        if result.action == "CHANGE_TAB":
            if result.target is not None:
                tabbed_content.active = result.target

            # Cambia de estado
        elif result.action == "SWITCH_STATE":
            if result.target == "game":
                tabbed_content.active = "game"
            elif result.target == "menu":
                tabbed_content.active = "profile"


if __name__ == "__main__":
    app = AppNavegacionPorTexto()
    app.run()
