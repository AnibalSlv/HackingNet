import random
from pathlib import Path


class Etc:
    def __init__(self):
        self.random = random.Random()
        self.list_file = ["configuracion.txt", "permisos.txt"]

    def generate_contents(self, base_path, seed):
        self.random.seed(seed)

        # Se copia la lista de archivos para que cada carpeta tenga sus propios archivos
        file_avalible = self.list_file.copy()

        # Crea entre 1 a 5 archivos maximo, si no hay 5 archivos entonces pasa como maximo
        # el valor de len(file_avalible)
        cant_file = random.randint(1, min(len(file_avalible), 8))

        select_file = random.sample(file_avalible, cant_file)

        dir = Path(base_path) / "etc"
        dir.mkdir(parents=True, exist_ok=True)

        for file_name in select_file:
            file_path = dir / file_name
            file_path.touch()  # .touch() crea el archivo vacío
        pass
