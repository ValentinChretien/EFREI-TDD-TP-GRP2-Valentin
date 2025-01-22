# EFREI - Groupe 2

Valentin Chrétien

## Programme - nasaRover.py

### Zone
- Crée une zone carrée de la taille spécifiée, initialisée avec des valeurs par défaut (0).
    ```python
    initialize_zone(size: int) -> List[List[Union[int, str]]]
    ```
- Affiche la zone dans la console avec (0, 0) représenté en bas à gauche.
    ```python
    print_zone(zone: List[List[int]]) -> None
    ```

### Rover
- Initialise les coordonnées et l'orientation d'un rover à partir d'une chaîne d'entrée.
    ```python
    pythoninit_rover(user_input: str) -> Tuple[int, int, str]
    ```

- Convertit les informations d'un rover (position et orientation) en une chaîne formatée.
    ```python
    rover_toString(rover: tuple[int, int, str]) -> str
    ```

- Applique une série de commandes pour déplacer un rover dans une zone tout en respectant les limites.
    ```python
    move_rover(zone_size: int, rover: tuple[int, int, str], commands: str) -> tuple[int, int, str]
    ```

### Global
- Affiche l'état global de la zone en montrant les positions actuelles des deux rovers (A et B).
    ```python
    print_global_state(zone: list[list[int]], rover_A: tuple[int, int, str], rover_B: tuple[int, int, str]) -> None
    ```
## Tests - nasaRover_test.py

Commande d'execution des tests unitaires (suite de 10 tests) : 
```python -m unittest nasaRover_test-unitaire.py```

Commande d'execution du tests de scenario (1 test) : 
```python -m unittest nasaRover_test-scenario.py```
