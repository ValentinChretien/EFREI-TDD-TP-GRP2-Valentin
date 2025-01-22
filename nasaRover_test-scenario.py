import unittest
from unittest.mock import patch
from io import StringIO
from nasaRover import initialize_zone, init_rover, move_rover, rover_toString, print_global_state

class TestRoverScenario(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        "5",            # Taille de la plateforme
        "1 2 N",        # Position initiale et orientation de Rover A
        "3 3 E",        # Position initiale et orientation de Rover B
        "LMLMLMLMM",    # Commandes pour Rover A
        "MMRMMRMRRM"    # Commandes pour Rover B
    ])
    @patch('sys.stdout', new_callable=StringIO)  # Capture de la sortie standard
    def test_complete_scenario(self, mock_stdout, mock_input):
        # Initialisation
        zoneSize = int(input("Précisez la taille de la plateforme : "))
        rover_A = init_rover(input("Initialisez la position et l'orientation de Rover A (format : x y orientation) : "))
        rover_B = init_rover(input("Initialisez la position et l'orientation de Rover B (format : x y orientation) : "))
        zone = initialize_zone(zoneSize)

        # Affichage Initialisation
        print(rover_toString(rover_A))
        print(rover_toString(rover_B))
        print_global_state(zone, rover_A, rover_B)

        # Interactions
        rover_A = move_rover(zoneSize, rover_A, input("Commandez le rover A : "))
        rover_B = move_rover(zoneSize, rover_B, input("Commandez le rover B : "))

        # Résultats finaux
        print(rover_toString(rover_A))
        print(rover_toString(rover_B))
        print_global_state(zone, rover_A, rover_B)

        # Vérification des résultats
        expected_output = (
            "1 2 N\n"
            "3 3 E\n"
            "\nÉtat global de la zone :\n"
            "0\t0\t0\t0\t0\n"
            "0\t0\t0\tB\t0\n"
            "0\tA\t0\t0\t0\n"
            "0\t0\t0\t0\t0\n"
            "0\t0\t0\t0\t0\n"
            "\n"
            "1 3 N\n"
            "5 1 E\n"
            "\nÉtat global de la zone :\n"
            "0\t0\t0\t0\t0\n"
            "0\t0\t0\t0\t0\n"
            "0\tA\t0\t0\t0\n"
            "0\t0\t0\t0\t0\n"
            "0\t0\t0\t0\tB\n"
            "\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
