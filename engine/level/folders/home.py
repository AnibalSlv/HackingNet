import random
from pathlib import Path


class Home:
    def __init__(self):
        self.random = random.Random()
        self.list_folder = [
            "Juan",
            "Wilmer",
            "Diego",
            "Maria",
            "Lucia",
            "Sofia",
            "Felix",
            "Pau",
            "Valeria",
            "Antonio",
            "Ana",
            "Anibal",
        ]

        self.list_file = [
            # Personal
            "emails.txt",
            "carta.txt",
            "cuentas.txt",
            "diario.txt",
            "cv_trabajo.pdf",
            # Relleno
            "foto.jpg",
            "tareas.txt",
            "borrador.txt",
            "contactos.txt",
            "whatssap.exe",
            "facebook.exe",
            "importante",
            # Pistas
            "contrasenas.txt",
        ]

    def generate_contents(self, base_path, seed):
        self.random.seed(seed)

        cant_folder = random.randint(1, len(self.list_folder))

        # Selecciona carpetas sin repetir
        select_folder = random.sample(self.list_folder, cant_folder)

        for folder_name in select_folder:
            folder = Path(base_path) / "home" / folder_name
            folder.mkdir(parents=True, exist_ok=True)

            # Se copia la lista de archivos para que cada carpeta tenga sus propios archivos
            file_avalible = self.list_file.copy()

            # Crea entre 1 a 5 archivos maximo, si no hay 5 archivos entonces pasa como maximo
            # el valor de len(file_avalible)
            cant_file = random.randint(1, min(len(file_avalible), 8))

            select_file = random.sample(file_avalible, cant_file)

            for file_name in select_file:
                file_path = folder / file_name
                file_path.touch()  # .touch() crea el archivo vacío
        pass
