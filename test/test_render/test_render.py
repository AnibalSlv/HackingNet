from textual.widgets import *
from textual.containers import *
from textual.app import App, ComposeResult

#from engine.player import Player

class TestApp(App):
    
    def __init__(self):
        super().__init__()
        #self.player = Player

    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        with Container(id="container-game"):
            # 1. Panel Izquierdo (Folder)
            with Container(id="panel-folder"):
                # 1. Creamos la raíz principal del sistema
                tree: Tree[str] = Tree("Sistema_Red", id="mi-arbol")
                tree.root.expand()

                # 2. Primera carpeta principal (Characters) y sus archivos
                characters = tree.root.add("Characters", expand=True)
                characters.add_leaf("Paul.usr")
                characters.add_leaf("Jessica.usr")
                characters.add_leaf("Chani.usr")

                # 3. Segunda carpeta principal (Logs) en el mismo nivel
                logs_folder = tree.root.add("System_Logs", expand=False) # expand=False para que empiece cerrada
                logs_folder.add_leaf("auth.log")
                logs_folder.add_leaf("connections.json")

                # 4. Tercera carpeta principal (Scripts de hackeo)
                tools_folder = tree.root.add("Exploits", expand=True)
                tools_folder.add_leaf("ssh_bruteforce.py")
                tools_folder.add_leaf("port_scanner.go")

                # 5. ¿Quieres una carpeta DENTRO de otra carpeta? (Subcarpeta)
                subcarpeta_credenciales = tools_folder.add("Credentials", expand=False)
                subcarpeta_credenciales.add_leaf("passwords.txt")

                # Finalmente, haces el yield de ese único árbol que ya contiene todo
                yield tree

            
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
                yield Label("C:/Users/.../Download>", id="lbl-prompt-path")
                yield Input(placeholder="Introduce un comando...", id="terminal-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
            comando = event.value.strip().lower

            if not comando:
                return

            terminal_log = self.query_one("#panel-log", RichLog)
            terminal_input = self.query_one("#terminal-input", Input)

            # Se agrega el comando al historial
            #terminal_log.write(f"{self.player.name}@hackingnet:~# {comando}")
            terminal_log.write(f"Anibal@hackingnet:~# {comando}")
            

            # Se procesan los comandos
            if comando == "help":
                terminal_log.write(" Comandos disponibles: help, status, clear, exit")
            elif comando == "clear":
                terminal_log.clear()
            else:
                terminal_log.write(f" Error: Comando '{comando}' no reconocido.")

            terminal_input.value = ""

    def on_mount(self,) -> None:
            lbl_hackback = self.query_one("#dashboard-hackback")
            lbl_hackback.border_title = "Hackback:"

            lbl_hackback = self.query_one("#dashboard-memory")
            lbl_hackback.border_title = "Memory:"

            lbl_bg_thread = self.query_one("#dashboard-bg-thread")
            lbl_bg_thread.border_title = "Process:"

if __name__ == "__main__":
    app = TestApp()
    app.run()