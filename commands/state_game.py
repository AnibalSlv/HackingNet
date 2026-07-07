from commands.definitions import CommandResult, TerminalState
from engine.binary_search_tree import Node, navegation_node, view_nodes


class GameState(TerminalState):
    def __init__(self, node: Node):
        self.node_current = node
        self.commands = {"ls": self._ls, "cd": self._cd, "salir": self._salir}

    def execute(self, command: str, args: list[str]) -> CommandResult:
        handler = self.commands.get(command)
        if handler:
            return handler(args)
        return CommandResult(f"Comando de juego '{command}' no válido.", error=True)

    def _ls(self, args: list[str]) -> CommandResult:

        result = view_nodes(self.node_current)
        output_formateado = "\n".join([nodo.name for nodo in result])

        print("-" * 20)
        print(
            f"DEBUG: node_current={self.node_current} | tipo={type(result)} | contenido={result}"
        )
        print("-" * 20)

        return CommandResult(
            output=f"Elementos de {self.node_current.name}:\n{output_formateado}"
        )

    def _cd(self, args: list[str]) -> CommandResult:

        if not args:
            return CommandResult("Especifica un nodo.", error=True)

        target_node_name = args[0]

        print("-"*30)
        print(f"{target_node_name}")
        print("-"*30)

        result = navegation_node(self.node_current, target_node_name)

        if result is None:
            return CommandResult(
                f"Directorio '{target_node_name}' no encontrado.", error=True
            )

        self.node_current, path_str = result
        return CommandResult(f"Ruta actual: {path_str}", path=f"{path_str}>")

    def _salir(self, args: list[str]) -> CommandResult:
        return CommandResult(
            "Saliendo del juego...", action="SWITCH_STATE", target="menu"
        )

