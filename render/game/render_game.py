from textual.widgets import *
from textual.widgets import *
from textual.containers import *
from textual.app import ComposeResult

class RenderGame(TabPane):
    def __init__(self, *args, **kwargs):
        super().__init__("Title" ,*args, id= "game", **kwargs)
        self.target_ip = None

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
            yield RichLog(id="panel-log", auto_scroll=True)
            
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
            with Vertical(id="panel-terminal"):
                # Aquí se irán mostrando los comandos ejecutados y outputs
                yield RichLog(id="terminal-log", max_lines=None, auto_scroll=True)
                # La línea de comandos real abajo
                yield Input(placeholder="Introduce un comando...", id="terminal-input")

    def on_input_submitted(self, event: Input.Submitted) -> None:
            # 1. Obtenemos el texto que escribió el usuario
            comando = event.value.strip()

            if not comando:
                return  # Si presionó enter vacío, no hacemos nada

            # 2. Obtenemos referencias a los widgets
            terminal_log = self.query_one("#terminal-log", RichLog)
            terminal_input = self.query_one("#terminal-input", Input)

            # 3. Añadimos el comando al historial (puedes meterle colores estilo terminal)
            terminal_log.write(f"usuario@hackingnet:~# {comando}")

            # 4. Aquí es donde procesas el comando en tu juego
            if comando == "help":
                terminal_log.write(" Comandos disponibles: help, status, clear, exit")
            elif comando == "clear":
                terminal_log.clear()
            else:
                terminal_log.write(f" Error: Comando '{comando}' no reconocido.")

            # 5. Limpiamos el Input para el siguiente comando
            terminal_input.value = ""

    def on_mount(self,) -> None:
            lbl_hackback = self.query_one("#dashboard-hackback")
            lbl_hackback.border_title = "Hackback:"

            lbl_hackback = self.query_one("#dashboard-memory")
            lbl_hackback.border_title = "Memory:"

            lbl_bg_thread = self.query_one("#dashboard-bg-thread")
            lbl_bg_thread.border_title = "Process:"