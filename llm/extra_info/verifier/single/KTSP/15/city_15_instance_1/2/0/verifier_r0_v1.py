import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
            4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
            8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
            12: (83, 96), 13: (60, 50), 14: (98, 1)
        }
        self.tour = [0, 6, 1, 7, 3, 9, 0]
        self.reported_cost = 118

    def test_tour_requirements(self):
        tour = self.tour
        cities = self.cities
        
        # Test Requirement 1: Tour must include exactly 6 cities, including the depot
        self.assertEqual(len(set(tour)), 6, "Requirement 1: Tour should include exactly 6 cities")

        # Test Requirement 2: Tour must start and finish at the depot city (city 0)
        self.assertTrue(tour[0] == 0 and tour[-1] == 0, "Requirement 2: Tour should start and end at depot city")

        # Test Requirement 3: Check the calculated travel distance
        calculated_cost = 0
        for i in range(len(tour)-1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

        # Test Requirement 4: Given cost is the expected minimal cost
        self.assertEqual(self.reported_cost, calculated_cost, "Requirement 4: Travel cost should match reported cost")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)