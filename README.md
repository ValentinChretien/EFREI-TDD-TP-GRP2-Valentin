# EFREI - Groupe 2

Valentin Chrétien

## Programme - nasaRover.py

### Zone
```initialize_zone(size: int) -> List[List[Union[int, str]]]```
Crée une zone carrée de la taille spécifiée, initialisée avec des valeurs par défaut (0).

```print_zone(zone: List[List[int]]) -> None```
Affiche la zone dans la console avec (0, 0) représenté en bas à gauche.

### Rover
```init_rover(user_input: str) -> Tuple[int, int, str]```
Initialise les coordonnées et l'orientation d'un rover à partir d'une chaîne d'entrée.

```rover_toString(rover: tuple[int, int, str]) -> str```
Convertit les informations d'un rover (position et orientation) en une chaîne formatée.

```move_rover(zone_size: int, rover: tuple[int, int, str], commands: str) -> tuple[int, int, str]```
Applique une série de commandes pour déplacer un rover dans une zone tout en respectant les limites.

### Global
```print_global_state(zone: list[list[int]], rover_A: tuple[int, int, str], rover_B: tuple[int, int, str]) -> None```
Affiche l'état global de la zone en montrant les positions actuelles des deux rovers (A et B).

## Tests - nasaRover_test.py

Commande d'execution des tests unitaires (suite de 10 tests) : 
```python -m unittest nasaRover_test-unitaire.py```

Commande d'execution du tests de scenario (1 test) : 
```python -m unittest nasaRover_test-scenario.py```
