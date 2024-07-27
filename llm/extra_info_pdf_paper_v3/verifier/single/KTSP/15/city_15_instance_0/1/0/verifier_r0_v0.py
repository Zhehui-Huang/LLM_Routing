import unittest
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class TestRobotTour(unittest.TestCase):
    def test_tour_requirements(self):
        # Provided tour and cost
        tour = [0, 1, 10, 8, 0]
        reported_cost = 90.54
        
        # City coordinates
        coordinates = {
            0: (9, 93),
            1: (8, 51),
            10: (19, 65),
            8: (19, 76)
        }
        
        # Check if tour starts and ends at the depot city 0
        self.assertEqual(tour[0], 0, "Tour should start at the depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at the depot city 0")
        
        # Check if the tour visits exactly 4 cities
        self.assertEqual(len(tour), 5, "Tour should visit 5 elements including start and end at depot")
        
        # Check if each city is visited at most once except depot city
        unique_cities = set(tour)
        self.assertTrue(all(tour.count(city) == 1 for city in unique_cities if city != 0), "Each non-depot city must be visited at most once")
        
        # Check if the tour is as short as possible (Here we just recalculate the cost)
        calc_cost = sum(euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1], coordinates[tour[i+1]][0], coordinates[tour[i+1]][1]) for i in range(len(tour) - 1))
        calc_cost = round(calc_address_cost, 2)
        
        # Check if reported cost matches calculated cost
        self.assertAlmostEqual(reported_cost, calc_cost, places=2, msg="Reported cost should match the calculated cost")
        
        # Check if format is correct ([0, ..., 0], cost)
        self.assertIsInstance(tour, list, "Tour should be a list")
        self.assertTrue(isinstance(reported_cost, (int, float)), "Total travel cost should be a number")
        
        # Final validation to make it pass or fail
        correct_conditions = (len(tour) == 5 and
                              tour[0] == 0 and
                              tour[-1] == 0 and
                              all(tour.count(city) == 1 for city in unique_cities if city != 0) and
                              abs(reported_cost - calc_cost) < 0.01)
        
        if correct_conditions:
            print("CORRECT")
        else:
            print("FAIL")

# Run the test
unittest.main(argv=[''], verbosity=2, exit=False)