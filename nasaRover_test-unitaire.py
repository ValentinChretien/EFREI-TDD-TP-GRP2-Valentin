import unittest
from typing import List, Tuple, Union
from nasaRover import initialize_zone, init_rover, move_rover, rover_toString, print_global_state

class TestRover(unittest.TestCase):
    # Tests pour initialize_zone
    def test_initialize_zone_valid(self):
        zone = initialize_zone(3)
        self.assertEqual(len(zone), 3)
        self.assertEqual(len(zone[0]), 3)
        self.assertEqual(zone, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_initialize_zone_invalid(self):
        with self.assertRaises(ValueError):
            initialize_zone(0)
        with self.assertRaises(ValueError):
            initialize_zone(-5)

    # Tests pour init_rover
    def test_init_rover_valid(self):
        rover = init_rover("1 2 N")
        self.assertEqual(rover, (1, 2, 'N'))

    def test_init_rover_invalid_format(self):
        with self.assertRaises(ValueError):
            init_rover("1 2")
        with self.assertRaises(ValueError):
            init_rover("1 2 NORTH")

    def test_init_rover_invalid_orientation(self):
        with self.assertRaises(ValueError):
            init_rover("1 2 Z")

    # Tests pour move_rover
    def test_move_rover_valid_commands(self):
        rover = (1, 1, 'N')
        rover = move_rover(5, rover, "M")
        self.assertEqual(rover, (1, 2, 'N'))

        rover = move_rover(5, rover, "R")
        self.assertEqual(rover, (1, 2, 'E'))

        rover = move_rover(5, rover, "M")
        self.assertEqual(rover, (2, 2, 'E'))

    def test_move_rover_out_of_bounds(self):
        rover = (0, 0, 'S')
        rover = move_rover(5, rover, "M")
        self.assertEqual(rover, (0, 0, 'S'))

        rover = (4, 4, 'N')
        rover = move_rover(5, rover, "M")
        self.assertEqual(rover, (4, 4, 'N'))

    def test_move_rover_invalid_commands(self):
        rover = (1, 1, 'N')
        rover = move_rover(5, rover, "X")
        self.assertEqual(rover, (1, 1, 'N'))  # Aucun effet attendu

    # Tests pour rover_toString
    def test_rover_toString(self):
        rover = (2, 3, 'W')
        self.assertEqual(rover_toString(rover), "2 3 W")

    # Tests pour print_global_state (vérification indirecte)
    def test_print_global_state(self):
        zone = initialize_zone(5)
        rover_A = (1, 2, 'N')
        rover_B = (3, 3, 'E')
        # Vérifie que la fonction s'exécute sans erreur
        print_global_state(zone, rover_A, rover_B)

if __name__ == '__main__':
    unittest.main()
