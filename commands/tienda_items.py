"""
Catálogo de items disponibles en la tienda.
Separado del render para que sea fácil agregar/quitar/editar items
sin tocar la lógica de la pestaña.
"""

ITEMS_TIENDA = [
    {
        "id": "nmap",
        "nombre": "Nmap",
        "tipo": "herramienta",
        "precio": 300,
        "descripcion": "Escaneo de puertos y servicios",
    },
    {
        "id": "sqlmap",
        "nombre": "SQLmap",
        "tipo": "herramienta",
        "precio": 450,
        "descripcion": "Inyección SQL automatizada",
    },
    {
        "id": "john",
        "nombre": "John the Ripper",
        "tipo": "herramienta",
        "precio": 500,
        "descripcion": "Fuerza bruta de contraseñas",
    },
    {
        "id": "overclock",
        "nombre": "Overclock de CPU",
        "tipo": "mejora",
        "precio": 600,
        "descripcion": "+20% velocidad de ataque",
    },
    {
        "id": "vpn",
        "nombre": "VPN Premium",
        "tipo": "mejora",
        "precio": 500,
        "descripcion": "Reduce probabilidad de ser detectado",
    },
]


def buscar_item(item_id: str) -> dict | None:
    """Busca un item del catálogo por su id. Devuelve None si no existe."""
    for item in ITEMS_TIENDA:
        if item["id"] == item_id:
            return item
    return None
