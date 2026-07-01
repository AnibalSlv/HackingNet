def command_help(context_game) -> None:
    context_game.notify("Muestra los comandos existententes", title="HackingNet")

def command_ls(context_game) -> None:
    context_game.notify("Tengo que pensar esto", title="HackingNet")

def command_exit(context_game) -> None:
    context_game.exit()

command_global = {
    "help" : command_help,
    "cd" : "",
    "ls" : command_ls,
    "exit": command_exit,
}