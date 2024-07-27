import math
import unittest

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91),
            4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
            8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
            12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23),
            16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
        }
        self.groups = {
            0: [5, 6, 7, 11, 17],
            1: [1, 4, 8, 13, 16],
            2: [2, 10, 15, 18, 19],
            3: [3, 9, 12, 14]
        }
        self.proposed_solution = [0, 6, 13, 2, 9, 0]
        self.proposed_cost = 114.66
    
    def test_total_number_of_cities(self):
        self.assertEqual(len(self.cities), 20)
    
    def test_depot_city_coordinates(self):
        self.assertEqual(self.cities[0], (14, 77))

    def test_given_coordinates_match(self):
        self.assertEqual(self.cities[3], (14, 91))  # Check sample to ensure cities coordinates are correct

    def test_groups_membership(self):
        # Check if any city is in more than one group or missing
        all_cities_from_groups = sum(self.groups.values(), [])
        unique_cities_in_groups = set(all_cities_from_groups)
        self.assertEqual(len(all_cities_from_groups), len(unique_cities_in_groups))
        self.assertIn(13, self.groups[1])  # Checking one example for the groups

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_solution[0], 0)
        self.assertEqual(self.proposed_solution[-1], 0)

    def test_tour_visits_one_city_per_group(self):
        visited = set(self.proposed_solution[1:-1])
        for group, members in self.groups.items():
            self.assertTrue(any(city in visited for city in members))

    def test_calculated_travel_cost(self):
        tour = self.proposed_solution
        total_cost = sum(calculate_distance(self.cities[tour[i]], self.cities[tour[i + 1]]) 
                         for i in range(len(tour) - 1))
        self.assertAlmostEqual(total_cost, self.proposed_cost, places=2)

unittest.main(argv=[''], exit=False)