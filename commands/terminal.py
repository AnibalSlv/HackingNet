from typing import Optional

from commands.definitions import CommandResult
from commands.game_input_state import GameInputState
from commands.menu_input_state import MenuInputState


class Terminal:
    def __init__(self):

        self.states = {
            "menu": MenuInputState(),
            "game": GameInputState(),
        }

        self.current_state = self.states["menu"]

    def execute(self, input_user) -> Optional[CommandResult]:
        parts = input_user.strip().split()

        if not parts:
            return None

        command, args = parts[0], parts[1:]

        result = self.current_state.execute(command, args)

        if result and result.action == "SWITCH_STATE" and result.target in self.states:
            self.current_state = self.states[result.target]

        return result

    # Cambia el estado de la terminal (principalmente es para el render_game)
    def change_state(self, state_name: str) -> None:
        if state_name in self.states:
            self.current_state = self.states[state_name]
