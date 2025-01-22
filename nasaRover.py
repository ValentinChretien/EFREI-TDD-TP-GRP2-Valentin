from typing import List, Tuple, Union

#####
# Zone
#####

def initialize_zone(size: int) -> List[List[Union[int, str]]]:
    if size <= 0:
        raise ValueError("La taille du plateau doit être un entier positif.")
    return [[0 for _ in range(size)] for _ in range(size)]

def print_zone(zone: List[List[int]]) -> None:
    for row in reversed(zone):  # Inverse les lignes pour que (0, 0) soit en bas
        print("\t".join(map(str, row))+"\n")

#####
# Rover
#####

def init_rover(user_input: str) -> Tuple[int, int, str]:
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
    
def rover_toString(rover: tuple[int, int, str]) -> str:
    x, y, orientation = rover
    return f"{x} {y} {orientation}"

    
def move_rover(zone_size: int, rover: tuple[int, int, str], commands: str) -> tuple[int, int, str]:
    x, y, orientation = rover

    # Dictionnaire pour déterminer la nouvelle orientation après un pivot
    orientation_map = {
        'N': {'L': 'W', 'R': 'E'},
        'E': {'L': 'N', 'R': 'S'},
        'S': {'L': 'E', 'R': 'W'},
        'W': {'L': 'S', 'R': 'N'}
    }

    # Dictionnaire pour les mouvements en fonction de l'orientation
    movement_map = {
        'N': (0, 1),  # Déplacement vers le haut
        'E': (1, 0),  # Déplacement vers la droite
        'S': (0, -1), # Déplacement vers le bas
        'W': (-1, 0)  # Déplacement vers la gauche
    }

    # Parcourir les commandes et les exécuter
    for command in commands:
        if command == 'L' or command == 'R':
            orientation = orientation_map[orientation][command]
        elif command == 'M':
            dx, dy = movement_map[orientation]
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < zone_size and 0 <= new_y < zone_size:
                x, y = new_x, new_y
            #else:
            #    print(f"Le rover a atteint une limite à ({x}, {y}), mouvement ignoré.")
        #else:
            #print(f"Commande inconnue : {command}, ignorée.")

    return x, y, orientation

#####
# Global
#####    
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
rover_A = init_rover(input("Initialisez la position et l'orientation de Rover A (format : x y orientation) : "))
rover_B = init_rover(input("Initialisez la position et l'orientation de Rover B (format : x y orientation) : "))

zone = initialize_zone(zoneSize)

# Affichage Initialisation
#print_zone(zone)
print(rover_toString(rover_A))
print(rover_toString(rover_B))
print_global_state(zone, rover_A, rover_B)

# Interactions

rover_A = move_rover(zoneSize, rover_A, input("Commandez le rover A : "))
rover_B = move_rover(zoneSize, rover_B, input("Commandez le rover B : "))

# Result
print(rover_toString(rover_A))
print(rover_toString(rover_B))
print_global_state(zone, rover_A, rover_B)
