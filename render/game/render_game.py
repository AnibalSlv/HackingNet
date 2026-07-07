from pathlib import Path
from textual.widgets import *
from textual.widgets import *
from textual.containers import *
from textual.app import ComposeResult

from commands.terminal import Terminal
from commands.state_game import GameState
from engine.binary_search_tree import root_main
from engine.player import Player
class RenderGame(TabPane):
    def __init__(self, *args, **kwargs):
        super().__init__("Title" ,*args, id= "game", **kwargs)
        self.target_ip = None
        self.root_node = root_main
        self.player = Player()

        self.terminal = Terminal()
        self.terminal.change_state("game")

    DEFAULT_CSS = (Path(__file__).parent / "style.tcss").read_text(encoding="utf-8")

    def compose(self) -> ComposeResult:
        with Container(id="container-game"):
            # 1. Panel Izquierdo (Folder)
            with Container(id="panel-folder"):
                yield DirectoryTree("engine/folder_of_game/prueba01")

            
            # 2. Panel Central Superior (Logs)
            yield RichLog(id="panel-log", max_lines=None, auto_scroll=True)

            
            # 3. Panel Derecho (Dash-Board)
            with Vertical(id="panel-dashboard"):
                yield Static("Dash Board", id="dashboard-title")

                with Horizontal(id="container-memory"):
                    yield Static("0 GB / 4 GB", id="dashboard-memory")
                
                with Horizontal(id="container-hackback"):
                    yield Static("0%", id="dashboard-hackback")
                
                with Container(id="container-bg-thread"):
                    with Vertical(id="dashboard-bg-thread"):
                        with Vertical():
                            yield Static("Proceso 1: 0%")
                            yield Static("Proceso 2: 0%")
                            yield Static("Proceso 3: 0%")
                            yield Static("Proceso 4: 0%")
            
            # 4. Panel Inferior (Terminal)
            with Horizontal(id="panel-terminal"):
                yield Label("", id="lbl-prompt-path")
                yield Input(placeholder="Introduce un comando...", id="terminal-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        comando = event.value

        if not comando:
            return

        terminal_log = self.query_one("#panel-log", RichLog)
        terminal_input = self.query_one("#terminal-input", Input)
        terminal_lbl = self.query_one("#lbl-prompt-path", Label)

        # 1. El motor procesa el comando en la capa lógica correspondiente (GameState, MenuState, etc.)
        result = self.terminal.execute(comando)

        # 2. Pintamos la línea del Prompt en el Log (Estilo Linux)
        terminal_log.write(f"{self.player.name}@hackingnet:~# {comando}")

        # 3. Dejamos que el motor decida qué imprimir en base al resultado
        if result.error:
            terminal_log.write(f" [red]Error: {result.output}[/red]")
        else:
            if result.output:
                terminal_log.write(result.output)
                if result.path != None:
                    terminal_lbl.update(result.path)

        # 4. Limpieza y fijación estricta del FOCO para evitar congelamientos de la UI
        terminal_input.value = ""
        event.input.focus()

    def on_mount(self,) -> None:
            lbl_hackback = self.query_one("#dashboard-hackback")
            lbl_hackback.border_title = "Hackback:"

            lbl_hackback = self.query_one("#dashboard-memory")
            lbl_hackback.border_title = "Memory:"

            lbl_bg_thread = self.query_one("#dashboard-bg-thread")
            lbl_bg_thread.border_title = "Process:"
