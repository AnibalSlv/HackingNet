from commands.definitions import CommandResult, TerminalState


class MenuState(TerminalState):
    def __init__(self):
        self.commands = {
            "cd": self._cd,
            "ls": self._ls,
        }

    def execute(self, command, args) -> CommandResult:
        handler = self.commands.get(command)

        if handler:
            return handler(args)
        return CommandResult("Comando no reconocido en el menu", error=True)

    def _ls(self, args) -> CommandResult:
        return CommandResult("Pestanas Disponibles: red, profile, tienda")

    def _cd(self, args) -> CommandResult:
        if not args:
            return CommandResult("Especifique su destino", error=True)

        destination = args[0]
        if destination == "game":
            return CommandResult(
                "Iniciando Juego...", action="SWITCH_STATE", target="game"
            )
        elif destination in ["red", "profile"]:
            return CommandResult(
                f"Cambiando a {destination}", action="CHANGE_TAB", target=destination
            )

        return CommandResult("Destino no encontrado", error=True)
