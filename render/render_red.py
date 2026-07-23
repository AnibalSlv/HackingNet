from textual.widgets import *
from textual.containers import Grid
from render.game.render_game import RenderGame

from commands.red_commands import command_red
from render.ip_utils import generar_red_disponible, generar_dificultad


class RenderRed(TabPane):
    def __init__(self) -> None:
        super().__init__("Red", id="red")
        # Genera una lista nueva de IPs "hackeables" cada vez que se abre la pestaña
        self.ips_disponibles = generar_red_disponible(cantidad=5)

    def compose(self):
        yield Static("Bienvenido a la Red *Emoji calavera*")

        with Grid(id="grid_red"):
            # Encabezados
            yield Static("IP", classes="header_red")
            yield Static("Firewall", classes="header_red")
            yield Static("Dificultad", classes="header_red")
            yield Static("Recompensa", classes="header_red")

            # Filas de datos, una IP por fila (4 celdas cada una)
            for ip in self.ips_disponibles:
                stats = generar_dificultad(ip)
                color = self._color_por_dificultad(stats["dificultad"])

                yield Static(f"[bold]{ip}[/]", classes="celda_red")
                yield Static(stats["firewall"], classes="celda_red")
                yield Static(f"[{color}]{stats['dificultad']}/10[/{color}]", classes="celda_red")
                yield Static(f"${stats['recompensa']}", classes="celda_red")

        yield Input(placeholder="", id="buscador_pestanas")

    @staticmethod
    def _color_por_dificultad(nivel: int) -> str:
        if nivel <= 3:
            return "#00ff41"   # verde neón - fácil
        elif nivel <= 6:
            return "#ffcc00"   # ámbar - medio
        return "#ff3333"       # rojo - difícil

    def on_input_submitted(self, event: Input.Submitted):
        inputUser = event.value.strip().lower().split()
        event.input.value = ""  # limpia el input apenas se envía el comando

        command = inputUser[0]

        if command in command_red:
            if len(inputUser) < 2:
                self.notify("Debes especificar una red. Ejemplo: cat 123.456.7.8", severity="error")
                return

            target_ip = inputUser[1]

            if target_ip not in self.ips_disponibles:
                self.notify("Esa IP no está disponible en esta red.", severity="error")
                return

            tabbed_content = self.app.query_one("#windows", TabbedContent)
            render_game = self.app.query_one("#game")
            render_game.updateValueIp(target_ip)
            tabbed_content.active = "game"
