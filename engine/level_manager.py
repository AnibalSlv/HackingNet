from pathlib import Path

from engine.rng_manager import RNGManager


class LevelManager:
    """
    Rules:
        /etc (Configuraciones del sistema):
            contraseñas olvidadas por administradores descuidados en archivos de configuración.

        /var/logs (Registro de actividad):
            para que el jugador busque pistas de accesos anteriores, IPs o reportes de errores del sistema.

        /home (Directorios de usuarios):
            Las carpetas personales de los empleados o administradores de la máquina que se hackea.

        /root (Directorio del administrador):
            La carpeta ultra protegida donde suele estar el "objetivo" final o los archivos más confidenciales.

        /dev (Devices / Dispositivos Físicos): <--------- Por pensar bien
           En Linux, todo es un archivo. Las tarjetas de video, los discos duros y los teclados se representan como
           archivos dentro de /dev. Por ejemplo, /dev/sda es el primer disco duro físico.

        / (Raíz del servidor)
        ├── bin/      # HERRAMIENTAS Y COMANDOS (Para ejecutar programas) <-- Para pensar
        ├── etc/      # SECRETOS Y CREDENCIALES (Para robar contraseñas)
        ├── var/      # EL RASTRO (Para borrar los logs y huellas) <-- Si no limpia sus huellas pierde porque lo rastrean
        │   └── log/
        ├── home/        # NARRATIVA Y LORE (Para leer archivos personales)
        └── sys/ o dev/  # EL NÚCLEO (Para tumbar o destruir el servidor) <-- Se podria utilizar como una opcion
            "kamikaze", si no tiene tiempo de limpiar los rastros, tira el servidor pero quizas no obtenga la recompensa
    """

    roots = ["etc", "var", "home", "root", "bin"]
    sub_roots = {"/etc": [""]}

    def __init__(self, rng: RNGManager):
        self.rng = rng

    def folder_of_game(self):

        folder = Path("servidor")  # <--- Deberia de ser aleatorio
        folder.mkdir(
            exist_ok=True
        )  # exist_ok evita errores si ya existe y crea la carpeta

        # Se crean las carpetas
        for root in self.roots:
            folder = Path("engine") / "folder_of_game" / "server" / root
            folder.mkdir(parents=True, exist_ok=True)

        # Se crea el archivo importante para terminar la partida
        file = (
            Path("engine") / "folder_of_game" / "server" / "root" / "password_admin.txt"
        )

        file.parent.mkdir(parents=True, exist_ok=True)

        # 2. Ahora sí, escribe la contraseña hardcodeada con seguridad
        file.write_text("password: 1234")

        file_name = file.as_posix()
        # Se guardan los archivos encriptados para poder agregar status y password
        list_file_enc: dict[str, dict[str, str]] = {
            file_name: {"status": "locked", "password": "1234"}
        }

        # Retorna el diccionario para que el Core pueda tener acceso
        return list_file_enc

    def archives_enc(self):
        pass
