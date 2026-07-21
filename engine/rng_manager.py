import random


class RNGManager:
    def __init__(self, seed: int = 0):
        self.random_instance = random.Random(seed)

    def generate_archives(self, file, folder):
        pass
