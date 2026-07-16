from commands.definitions import CommandResult, TerminalState
from engine.archive_enc import archive_enc_real
from engine.binary_search_tree import Node, navegation_node, view_nodes


class GameInputState(TerminalState):
    def __init__(self, node: Node):
        self.node_current = node

        self.arcvhibe_enc = archive_enc_real
        self.commands = {
            "ls": self._ls,
            "cd": self._cd,
            "cat": self._cat,
            "salir": self._salir,
        }

    def execute(self, command: str, args: list[str]) -> CommandResult:
        handler = self.commands.get(command)
        if handler:
            return handler(args)
        return CommandResult(f"Comando de juego '{command}' no válido.", error=True)

    def _ls(self, args: list[str]) -> CommandResult:

        result = view_nodes(self.node_current)
        output_formateado = "\n".join([nodo.name for nodo in result])

        return CommandResult(
            output=f"Elementos de {self.node_current.name}:\n{output_formateado}"
        )

    def _cd(self, args: list[str]) -> CommandResult:

        if not args:
            return CommandResult("Especifica un nodo.", error=True)

        target_node_name = args[0]

        result = navegation_node(self.node_current, target_node_name)

        if result is None:
            return CommandResult(
                f"Directorio '{target_node_name}' no encontrado.", error=True
            )

        self.node_current, path_str = result
        return CommandResult(f"Ruta actual: {path_str}", path=f"{path_str}>")

    def _cat(self, args: list[str]) -> CommandResult:
        if not args:
            return CommandResult("Especifica un archivo.", error=True)

        name_file = args[0]

        # Busca primero la configuración del archivo usando su nombre como clave
        info_file: dict[str, str] | None = self.arcvhibe_enc.arhives_enc.get(name_file)

        # Si el usuario ingresó una contraseña (ej: cat password_admin.txt 1234)
        if len(args) > 1:
            input_password = args[1]

            # Verifica si el archivo existe en nuestro registro de encriptados
            if info_file is not None:
                # Extrae la contraseña específica de ese archivo
                password_file = info_file.get("password")

                if input_password == password_file:
                    return CommandResult(
                        f"Accediendo al archivo {name_file}...\n[CONTENIDO DESBLOQUEADO: password: {input_password}]"
                    )
                else:
                    return CommandResult("Contraseña incorrecta.", error=True)
            else:
                return CommandResult(
                    "Este archivo no requiere contraseña o no existe.", error=True
                )

        # Si solo se escribió el nombre del archivo (sin contraseña)
        # (objeto donde buscar, el valor que buscar, si no tiene el valor devuelve este otro)
        if name_file == getattr(self.arcvhibe_enc, "try_access", None):
            return CommandResult("Accediendo al archivo")

        return CommandResult("No se puede acceder al archivo", error=True)

    def _salir(self, args: list[str]) -> CommandResult:
        return CommandResult(
            "Saliendo del juego...", action="SWITCH_STATE", target="menu"
        )
