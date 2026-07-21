from pathlib import Path

from engine.level.folders import Bin, Data, Etc, Home, Root, Temp
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

    def __init__(self, rng: RNGManager):
        self.rng = rng
        self.temp_seed = 0

    def folder_of_game(self):

        base_path = "engine/folder_of_game/server/"

        Bin().generate_contents(base_path, self.temp_seed)
        Data().generate_contents(base_path, self.temp_seed)
        Etc().generate_contents(base_path, self.temp_seed)
        Home().generate_contents(base_path, self.temp_seed)
        Root().generate_contents(base_path, self.temp_seed)
        Temp().generate_contents(base_path, self.temp_seed)

        # Se crea el archivo importante para terminar la partida
        file = (
            Path("engine") / "folder_of_game" / "server" / "root" / "password_admin.txt"
        )

        file.parent.mkdir(parents=True, exist_ok=True)

        # 2. Ahora sí, escribe la contraseña hardcodeada con seguridad
        file.write_text("password: 1234")

        # .as_posix() devuelve la posicion del archivo en un formato en el que se puede acceder (/)
        file_name = file.as_posix()
        # Se guardan los archivos encriptados para poder agregar status y password
        list_file_enc: dict[str, dict[str, str]] = {
            file_name: {"status": "locked", "password": "1234"}
        }

        # Retorna el diccionario para que el Core pueda tener acceso
        return list_file_enc

    def archives_enc(self):
        pass
