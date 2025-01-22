from typing import List

def initialize_zone(size: int) -> List[List[Union[int, str]]]:
    if size <= 0:
        raise ValueError("La taille du plateau doit être un entier positif.")
    return [[0 for _ in range(size)] for _ in range(size)]

def print_zone(zone: List[List[int]]) -> None:
    for row in reversed(zone):  # Inverse les lignes pour que (0, 0) soit en bas
        print("\t".join(map(str, row))+"\n")

# Initialisation
zoneSize = int(input("Précisez la taille de la plateforme : "))
zone = initialize_zone(zoneSize)

# Affichage
print_zone(zone)