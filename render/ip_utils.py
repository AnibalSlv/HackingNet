"""
Utilidades para generar IPs "hackeables" de forma pseudoaleatoria,
usando los propios números de la IP (IPv4) como semilla para que
cada objetivo tenga stats consistentes (misma IP = mismo reto).
"""

import random


def generar_ip_aleatoria() -> str:
    """
    Genera una IPv4 con 4 octetos (0-255), evitando rangos reservados
    o poco creíbles para el juego (loopback, privadas clase A, multicast).
    """
    while True:
        octetos = [random.randint(1, 254) for _ in range(4)]
        primero = octetos[0]

        # Evita 127.x (loopback), 10.x (privada), 224+ (multicast/reservado)
        if primero in (10, 127) or primero >= 224:
            continue

        return ".".join(str(o) for o in octetos)


def ip_a_semilla(ip: str) -> int:
    """Convierte una IP tipo '192.168.1.15' en un entero único para usar como semilla."""
    partes = ip.split(".")
    return (
        int(partes[0]) * 256**3
        + int(partes[1]) * 256**2
        + int(partes[2]) * 256
        + int(partes[3])
    )


def generar_red_disponible(cantidad: int = 5) -> list[str]:
    """Genera una lista de IPs distintas para mostrar como objetivos disponibles."""
    ips: set[str] = set()
    while len(ips) < cantidad:
        ips.add(generar_ip_aleatoria())
    return list(ips)


def generar_dificultad(ip: str) -> dict:
    """
    Usa la IP como semilla para generar stats reproducibles de ese objetivo:
    la misma IP siempre da la misma dificultad/firewall/recompensa,
    pero IPs distintas dan combinaciones distintas.
    """
    semilla = ip_a_semilla(ip)
    rng = random.Random(semilla)  # generador local: no altera el random global del juego

    return {
        "dificultad": rng.randint(1, 10),
        "recompensa": rng.randint(50, 1000),
        "firewall": rng.choice(["débil", "medio", "fuerte", "militar"]),
    }
