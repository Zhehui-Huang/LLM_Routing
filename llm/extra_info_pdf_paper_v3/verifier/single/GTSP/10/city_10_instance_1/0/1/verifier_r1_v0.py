import unittest
from math import sqrt

# This function calculates the Euclidean distance between two cities given their coordinates
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.depot = (53, 68)
        self.cities = {
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        self.groups = [
            [5, 6, 7],
            [2, 3],
            [1, 9],
            [4, 8]
        ]
        # Provided solution
        self.solution_tour = [0, 9, 5, 3, 8, 0]
        self.actual_cost = 169.9409598467532

    def test_start_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at the depot.")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at the depot.")
    
    def test_one_city_per_group(self):
        visited = []
        for city in self.solution_tour[1:-1]:  # Skip the depot at the start and end
            found = False
            for group in self.groups:
                if city in group:
                    found = True                    
            self.assertTrue(found, f"City {city} must be from one of the groups.")
            visited.append(city)
        unique_groups_visited = len(set([city for group in self.groups for city in group if city in visited]))
        self.assertEqual(unique_groups_visited, 4, "Must visit exactly one city from each group.")
    
    def test_correct_travel_cost(self):
        calculated_cost = 0
        for i in range(len(self.solution_tour) - 1):
            if self.solution_tour[i] == 0:
                city_coords1 = self.depot
            else:
                city_coords1 = self.cities[self.solution_tour[i]]

            if self.solution_tour[i+1] == 0:
                city_coords2 = self.depot
            else:
                city_coords2 = self.cities[self.solution_tour[i+1]]

            calculated_cost += euclidean_distance(city_coords1, city_coords2)

        self.assertAlmostEqual(calculated_cost, self.actual_cost, places=5, msg="Calculated tour cost must match given total cost.")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)