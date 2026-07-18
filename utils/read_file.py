def read(file_read) -> str:
    with open(file_read, "r") as archivo:
        result = archivo.read()
    return result
