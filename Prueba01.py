from textual.app import App, ComposeResult
from textual.widgets import *

class MyFirstApp(App):
    """Esto es una prueba"""

    # Definir estilos o configuraciones globales
    BINDINGS = [("d", "toggle_dark", "Cambiar modo")]

    #? Es fundamental no se pq
    def compose(self) -> ComposeResult:
        """Aqui se define que va en la pantalla"""
        yield Header()
        yield Static("Good Night World")

        yield Input(placeholder="Escribe algo aquí y presiona Enter...", id="entrada_usuario")
        
        # Un texto estático para mostrar lo que el usuario escribió
        yield Static("Esperando que escribas...", id="pantalla_resultado")

        #yield Button("Presioname", variant="success", id="my_button")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        """Este metodo se ejecutal al presionar cualquier boton"""
        if event.button.id == "my_button":
            self.query_one(Static).update("You touch the button")

    # Se dispara cuando el usuario presiona enter
    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Este método se dispara automáticamente al presionar Enter."""
        
        # Obtenemos el texto que escribió el usuario
        texto_ingresado = event.value
        
        # Buscamos el widget de resultado y lo actualizamos
        self.query_one("#pantalla_resultado", Static).update(
            f"El usuario escribió: [bold cyan]{texto_ingresado}[/]"
        )
        
        # (Opcional) Limpiar el input después de enviar
        self.query_one("#entrada_usuario", Input).value = ""
        
if __name__ == "__main__":
    app = MyFirstApp()
    app.run()