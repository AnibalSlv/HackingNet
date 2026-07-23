from textual.widgets import *
from textual.containers import Grid

from commands.tienda_items import ITEMS_TIENDA, buscar_item


class RenderTienda(TabPane):
    def __init__(self, player) -> None:
        super().__init__("Tienda", id="tienda")
        self.player = player

    def compose(self):
        yield Static("[bold]Bienvenido a la Tienda[/] - usa: comprar <id>")

        with Grid(id="grid_tienda"):
            # Encabezados
            yield Static("ID", classes="header_tienda")
            yield Static("Nombre", classes="header_tienda")
            yield Static("Tipo", classes="header_tienda")
            yield Static("Precio", classes="header_tienda")
            yield Static("Descripción", classes="header_tienda")

            for item in ITEMS_TIENDA:
                color = "#00ff41" if item["tipo"] == "herramienta" else "#ffcc00"
                yield Static(item["id"], classes="celda_tienda")
                yield Static(item["nombre"], classes="celda_tienda")
                yield Static(f"[{color}]{item['tipo']}[/{color}]", classes="celda_tienda")
                yield Static(f"${item['precio']}", classes="celda_tienda")
                yield Static(item["descripcion"], classes="celda_tienda")

        yield Static(f"[green]Dinero disponible: ${self.player.money}[/]", id="dinero_tienda")
        yield Input(placeholder="", id="buscador_pestanas")

    def on_input_submitted(self, event: Input.Submitted):
        inputUser = event.value.strip().lower().split()
        event.input.value = ""  # limpia el input apenas se envía el comando

        if not inputUser:
            return

        command = inputUser[0]

        if command == "comprar":
            if len(inputUser) < 2:
                self.notify("Debes especificar un item. Ejemplo: comprar nmap", severity="error")
                return

            item_id = inputUser[1]
            item = buscar_item(item_id)

            if item is None:
                self.notify(
                    f"Item '{item_id}' no existe. Revisa la tabla de arriba.",
                    severity="warning",
                )
                return

            if self.player.money < item["precio"]:
                self.notify(
                    f"No tienes suficiente dinero para {item['nombre']} (cuesta ${item['precio']}).",
                    severity="error",
                )
                return

            # --- Aplicar la compra ---
            # NOTA: ajusta esto según cómo esté estructurado tu Player en engine/core.py.
            # Aquí asumo que player.tools es una lista donde se pueden agregar herramientas,
            # y que las mejoras se guardan en una lista player.mejoras (creala si no existe).
            self.player.money -= item["precio"]

            if item["tipo"] == "herramienta":
                if isinstance(self.player.tools, list):
                    self.player.tools.append(item["nombre"])
                else:
                    # Si tools es un string (como en el mock), lo convierte en algo legible
                    self.player.tools = f"{self.player.tools}, {item['nombre']}"
            else:
                if not hasattr(self.player, "mejoras"):
                    self.player.mejoras = []
                self.player.mejoras.append(item["nombre"])

            self.notify(f"Compraste {item['nombre']} por ${item['precio']}.", severity="information")

            # Refresca el texto de dinero disponible
            dinero_widget = self.query_one("#dinero_tienda", Static)
            dinero_widget.update(f"[green]Dinero disponible: ${self.player.money}[/]")
