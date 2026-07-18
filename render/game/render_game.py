from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.events.dto_events import DTOEvents

from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.message import Message
from textual.widgets import DirectoryTree, Input, Label, RichLog, Static, TabPane

from commands.terminal import Terminal
from engine.binary_search_tree import root_main
from engine.events.manager_events import manager_events
from engine.player import Player


class RenderGame(TabPane):
    def __init__(self, *args, **kwargs):
        super().__init__("Title", *args, id="game", **kwargs)
        self.target_ip = None
        self.root_node = root_main

        self.lbl_terminal_root = Label(str(self.root_node))

        self.player = Player()
        self.terminal = Terminal()
        self.manager_events = manager_events

        self.terminal.change_state("game")

    DEFAULT_CSS = (Path(__file__).parent / "style.tcss").read_text(encoding="utf-8")

    class RequestLoadGame(Message):
        pass

    # Actualiza la interfaz cuando se ejecuta un evento
    def update_interface(self, data: DTOEvents):
        lbl_hackback = self.query_one("#dashboard-hackback", Static)
        lbl_hackback.update((str(data.progress_event) + "%"))

    def on_show(self) -> None:
        # Suscribe el metodo update_interface para que los eventos tengas comunicacion con la UI
        self.manager_events.add_suscribers(self.update_interface)

        # Inicia el nivel
        self.post_message(self.RequestLoadGame())

        # Refresca el directorio de carpetas que vee el usuario
        tree = self.query_one(DirectoryTree)
        tree.reload()

        lbl_hackback = self.query_one("#dashboard-hackback")
        lbl_hackback.border_title = "Hackback:"
        lbl_hackback = self.query_one("#dashboard-memory")
        lbl_hackback.border_title = "Memory:"
        lbl_bg_thread = self.query_one("#dashboard-bg-thread")
        lbl_bg_thread.border_title = "Process:"

    def compose(self) -> ComposeResult:
        with Container(id="container-game"):
            # 1. Panel Izquierdo (Folder)
            with Container(id="panel-folder"):
                yield DirectoryTree("engine/folder_of_game/server")

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
                yield Label("server>", id="lbl-prompt-path")
                yield Input(placeholder="Introduce un comando...", id="terminal-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value
        new_command = None

        if not command:
            return

        terminal_log = self.query_one("#panel-log", RichLog)
        terminal_input = self.query_one("#terminal-input", Input)
        terminal_lbl = self.query_one("#lbl-prompt-path", Label)

        parts_command = command.split()

        # Transforma la direccion para poder utilizarlo
        if parts_command[0] == "cat":
            parts_command[1] = (
                "engine/folder_of_game/"
                + str(self.lbl_terminal_root)
                + "/"
                + parts_command[1]
            )
            new_command = " ".join(parts_command)

        if new_command is None:
            new_command = command

        # El motor procesa el comando en la capa lógica correspondiente (GameState)
        result = self.terminal.execute(new_command)

        # Crea el texto parseando el markup para poder tener colores
        text_color = Text.from_markup(
            f"[bold #ffffff]{self.player.name}[/][#777777]@hackingnet:~#[/] [#ffffff]{command}[/]"
        )
        terminal_log.write(text_color)

        if result is not None:
            if result.error:
                text_color = Text.from_markup(f"[red]Error: {result.output}[/red]")
                terminal_log.write(text_color)
            else:
                if result.output:
                    terminal_log.write(result.output)
                    if result.path:
                        terminal_lbl.update(result.path + ">")
                        self.lbl_terminal_root = result.path

        # Limpieza y fijación estricta del FOCO
        terminal_input.value = ""
        event.input.focus()
