from textual.app import App, ComposeResult
from textual.widgets import Input, TabbedContent

from commands.terminal import Terminal
from engine.archive_enc import archive_enc_real
from engine.player import Player
from render.game.render_game import RenderGame
from render.render_profile import RenderProfile
from render.render_red import RenderRed


class HackingGameApp(App):
    # Se agrega un poco de margen para que la interfaz respire visualmente
    CSS = """
    TabbedContent ContentTabs {
        display: none;
    }
    """

    def __init__(self):
        super().__init__()
        self.game = Core()
        self.terminal = Terminal()
        self.archive_enc = archive_enc_real
        # "/users/admin.txt" : {
        #   "status": "locked",
        #   "password": "a1234"
        # }

    def compose(self) -> ComposeResult:
        # El contenedor de pestañas con sus IDs definidos
        #! INITIAL ABRE POR DEFECTO LA PESTANA CON ESA ID
        with TabbedContent(initial="profile", id="windows"):
            yield RenderRed()
            yield RenderProfile(self.game.player)
            yield RenderGame()

    def on_render_game_request_load_game(self, event: RenderGame.RequestLoadGame):
        self.archive_enc.load_level()

    # Evento que se dispara al presionar Enter en el Input
    def on_input_submitted(self, event: Input.Submitted) -> None:
        texto_usuario = event.value
        result = self.terminal.execute(texto_usuario)
        event.input.value = ""

        if not result:
            return

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


class Core:
    def __init__(self):
        self.player = Player()

    def buy_item(self) -> None:
        self.player.money -= 10
