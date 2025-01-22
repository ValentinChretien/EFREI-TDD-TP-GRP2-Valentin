from typing import List, Tuple, Union

def initialize_zone(size: int) -> List[List[Union[int, str]]]:
    if size <= 0:
        raise ValueError("La taille du plateau doit être un entier positif.")
    return [[0 for _ in range(size)] for _ in range(size)]

def print_zone(zone: List[List[int]]) -> None:
    for row in reversed(zone):  # Inverse les lignes pour que (0, 0) soit en bas
        print("\t".join(map(str, row))+"\n")

def parse_rover_input(user_input: str) -> Tuple[int, int, str]:
    try:
        parts = user_input.strip().split()
        if len(parts) != 3:
            raise ValueError("L'entrée doit être au format 'x y z'.")
        
        x = int(parts[0])
        y = int(parts[1])
        
        z = parts[2].upper()
        if z not in {'N', 'E', 'S', 'W'}:
            raise ValueError("Orientation invalide. Veuillez entrer 'N', 'E', 'S' ou 'W'.")
        
        return x, y, z
    except ValueError as e:
        raise ValueError(f"Erreur lors de l'initialisation du rover : {e}")
    
def print_global_state(zone: list[list[int]], rover_A: tuple[int, int, str], rover_B: tuple[int, int, str]) -> None:
    size = len(zone)
    
    display_zone = [row[:] for row in zone]
    
    if 0 <= rover_A[1] < size and 0 <= rover_A[0] < size:
        display_zone[size - 1 - rover_A[1]][rover_A[0]] = 'A'
    if 0 <= rover_B[1] < size and 0 <= rover_B[0] < size:
        display_zone[size - 1 - rover_B[1]][rover_B[0]] = 'B'
    
    # Afficher la zone avec une tabulation pour l'alignement
    print("\nÉtat global de la zone :")
    for row in display_zone : 
        print("\t".join(str(cell) for cell in row)+"\n")



# Initialisation
zoneSize = int(input("Précisez la taille de la plateforme : "))
rover_A = parse_rover_input(input("Initialisez la position et l'orientation de Rover A (format : x y z) : "))
rover_B = parse_rover_input(input("Initialisez la position et l'orientation de Rover B (format : x y z) : "))

zone = initialize_zone(zoneSize)

# Affichage Initialisation
#print_zone(zone)
print_global_state(zone, rover_A, rover_B)

