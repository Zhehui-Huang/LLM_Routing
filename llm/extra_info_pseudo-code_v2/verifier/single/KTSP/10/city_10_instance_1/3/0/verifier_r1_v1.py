import unittest
import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates for the cities (Index corresponds to city number)
        self.cities = {
            0: (53, 68),
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
        # Provided tour and cost
        self.tour = [0, 7, 9, 5, 4, 0]
        self.provided_cost = 217.18
        
    def test_tour_starts_and_ends_at_depot(self):
        """Test that the tour starts and ends at depot city 0."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
        
    def test_tour_length(self):
        """Test that exactly 5 cities, including the depot, are visited."""
        self.assertEqual(len(set(self.tour)), 6)  # 5 different cities + depot visited
    
    def test_correct_computation_of_travel_cost(self):
        """Test that the travel cost is correctly calculated based on Euclidean distance."""
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city_1 = self.tour[i]
            city_2 = self.tour[i + 1]
            total_cost += calculate_euclidean_distance(self.cities[city_1], self.cities[city_2])
        # Check if the calculated total cost is approximately equal to the provided cost
        self.assertAlmostEqual(total_cost, self.provided_cost, places=2)

if __name__ == '__main__':
    unittest.main()