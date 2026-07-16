from engine.level_manager import LevelManager
from engine.rng_manager import RNGManager


class ArchiveEnc:
    def __init__(self):
        self.arhives_enc: dict[str, dict[str, str]] = {}
        self.rng = RNGManager(seed=0)
        self.level_manager = LevelManager(rng=self.rng)

    def _get_dict(self):
        pass

    def load_level(self) -> None:
        self.arhives_enc.update(self.level_manager.folder_of_game())

    def _try_access(self, input_user: str) -> bool:
        if input_user in self.arhives_enc:
            # Si el archivo tiene el estado "locked" el usuario no tiene acceso (por el not)
            return not self.arhives_enc[input_user]["locked"]
        return False

    def _unlock_file(self, root: str, password_user: str) -> bool:
        if root in self.arhives_enc:
            if password_user == self.arhives_enc[root]["password"]:
                self.arhives_enc[root]["status"] = "unlock"
                return True
        return False


archive_enc_real = ArchiveEnc()
