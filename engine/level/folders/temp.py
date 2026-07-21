import random
from pathlib import Path


class Temp:
    def __init__(self):
        self.random = random.Random()
        self.list_file = [
            # Distracciones
            "temp_001.tmp",
            "cache_01.tmp",
            "render.log",
            "datos_sesion.txt",
            "temp_021.tmp",
            # Resultados del comando scan
            "scan_result.txt",  # Resultado de haber usado el comando scan
            "descript_out.txt",  # Resultados de desencriptar algo
            "clipboard.txt",  # Contrasenas que el usuario guarda
        ]

    def generate_contents(self, base_path, seed):
        self.random.seed(seed)

        # Se copia la lista de archivos para que cada carpeta tenga sus propios archivos
        file_avalible = self.list_file.copy()

        # Crea entre 1 a 5 archivos maximo
        cant_file = random.randint(1, min(len(file_avalible), 8))
        select_file = random.sample(file_avalible, cant_file)

        # Definimos la ruta de la carpeta temp
        dir = Path(base_path) / "temp"
        dir.mkdir(parents=True, exist_ok=True)

        for file_name in select_file:
            file_path = dir / file_name
            file_path.touch()  # Ahora esto funcionará porque 'temp' ya existe
