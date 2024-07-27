import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 9, 5, 6, 0]
        self.reported_cost = 61.66

    def test_tour_length(self):
        # Check if the tour length includes exactly 4 cities plus return to the depot
        self.assertEqual(len(self.tour), 5)

    def test_tour_start_end(self):
        # Check if the tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_tour_cost(self):
        # Calculate the total travel cost
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            total_cost += calculate_distance(self.cities[city1], self.cities[city2])
        
        # Check if the total cost calculated matches the reported cost
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)