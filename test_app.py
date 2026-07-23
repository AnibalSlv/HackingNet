"""
Archivo de prueba para diseñar el .tcss con hot-reload.

Cómo usarlo:
1. Copia este archivo a la RAÍZ de tu proyecto (junto a las carpetas render/, commands/, engine/).
2. Copia también 'style.tcss' a la raíz (o ajusta CSS_PATH abajo).
3. Abre una terminal APARTE (no la integrada de VSCode).
4. Ejecuta:  textual run --dev test_app.py
5. Deja el archivo style.tcss abierto en tu editor y modifícalo:
    cada vez que guardes, la terminal se actualizará sola.

Nota: si RenderRed o RenderProfile fallan al importar (porque dependen de
otros módulos como command_red, RenderGame o Core), es porque este archivo
debe correr DESDE la raíz del proyecto real, no de forma aislada.
"""

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, Static
from textual.containers import Container

from render.render_red import RenderRed
from render.render_profile import RenderProfile
from render.render_tienda import RenderTienda


class MockPlayer:
    """Jugador falso solo para poder ver la pestaña Perfil con datos."""
    def __init__(self):
        self.name = "N30_Ghost"
        self.money = 1500
        self.prestige = 42
        self.tools = "Nmap, SQLmap, John the Ripper"
        self.ip_current = "192.168.1.15"


class ScanLine(Static):
    """Línea horizontal que se desliza de arriba hacia abajo dentro de su contenedor padre."""

    def __init__(self) -> None:
        super().__init__("")
        self._y = 0
        self._direction = 1

    def on_mount(self) -> None:
        self.set_interval(1 / 20, self._move)  # 20 pasos por segundo

    def _move(self) -> None:
        parent_height = self.parent.size.height if self.parent else 10
        if parent_height <= 1:
            return
        self._y += self._direction
        if self._y >= parent_height - 1 or self._y <= 0:
            self._direction *= -1
        self.styles.offset = (0, self._y)


class TestApp(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        player = MockPlayer()
        with TabbedContent(id="windows"):
            yield RenderRed()
            yield RenderProfile(player)
            yield RenderTienda(player)

    def on_mount(self) -> None:
        # Habilita la capa "overlay" en cada TabPane para que la ScanLine flote encima
        for pane_id in ("#red", "#profile", "#tienda"):
            pane = self.query_one(pane_id)
            pane.styles.layers = ("base", "overlay")
            pane.mount(ScanLine())

        self._glow_on = False
        self.set_interval(0.9, self._toggle_glow)

    def _toggle_glow(self) -> None:
        self._glow_on = not self._glow_on
        for pane_id in ("#red", "#profile", "#tienda"):
            pane = self.query_one(pane_id)
            pane.set_class(self._glow_on, "glow")



if __name__ == "__main__":
    TestApp().run()
