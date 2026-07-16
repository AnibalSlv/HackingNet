import os
from typing import Optional, Tuple

from anytree import NodeMixin
from anytree.resolver import ChildResolverError, Resolver


class Node(NodeMixin):  # <--- Heredar de NodeMixin
    def __init__(self, name, father=None, children=None):
        super(Node, self).__init__()
        self.name = name
        self.parent = father
        if children:
            self.children = children


# Función para armar el árbol internamente
def map_folder_tree(path_current, node_father=None):
    # Obtener el nombre de la carpeta o archivo
    name_current = os.path.basename(path_current)
    if not name_current:
        # Por si es una raíz como "C:\" o "/"
        name_current = path_current

    # Crear el nodo actual
    node_current = Node(name_current, father=node_father)

    # Si el nodo padre existe y la clase no lo vincula automáticamente:
    if node_father is not None:
        node_current.parent = node_father

    # Si es un directorio, explorar recursivamente
    if os.path.isdir(path_current):
        try:
            for element in os.listdir(path_current):
                path_son = os.path.join(path_current, element)
                map_folder_tree(path_son, node_current)
        except PermissionError:
            pass

    return node_current


# Carpeta contenedora
root_main = map_folder_tree("engine/folder_of_game/server")
resolver = Resolver("name")


# Ver el contenido del nodo actual
def view_nodes(node) -> list:
    node_current = node
    node_list = []

    for children in node_current.children:
        node_list.append(children)

    return node_list


def navegation_node(start_node: Node, target_name: str) -> Optional[Tuple[Node, str]]:
    try:
        # El Resolver busca directamente el nombre que escribió el usuario  desde la posición actual.
        target_node = resolver.get(start_node, target_name)

    except ChildResolverError:
        return None

    # Sirve como una seguridad para el analisis estatico
    if target_node is None:
        return None

    # Construye la guía visual de la ruta
    path_str = "/".join([node.name for node in target_node.path])

    # Retorna el nodo (para mantener la posición) y el str de guia
    return target_node, path_str
