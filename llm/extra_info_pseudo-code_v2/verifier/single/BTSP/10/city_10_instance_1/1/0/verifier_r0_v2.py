import unittest
import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
                       (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
        self.actual_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
        self.actual_total_cost = 291.41088704894975
        self.actual_max_distance = 56.61271941887264
    
    def test_tour_starts_and_ends_with_depot(self):
        """Test that the tour starts and ends at the depot city (city 0)."""
        self.assertEqual(self.actual_tour[0], 0)
        self.assertEqual(self.actual_tour[-1], 0)

    def test_tour_visits_each_city_once(self):
        """Test that the tour visits each city exactly once (except the depot city 0)."""
        visited = sorted(self.actual_tour[1:-1])
        expected_cities = list(range(1, 10))
        self.assertEqual(visited, expected_cities)
        
    def test_correct_total_travel_cost(self):
        """Test the total travel cost of the tour."""
        calculated_total_cost = sum(euclidean_distance(self.cities[self.actual_tour[i]], 
                                                       self.cities[self.actual_tour[i + 1]]) 
                                    for i in range(len(self.actual_tour) - 1))
        self.assertAlmostEqual(calculated_total_cost, self.actual_total_cost, places=5)

    def test_correct_max_distance_between_cities(self):
        """Test the maximum distance between consecutive cities in the tour."""
        distances = [euclidean_distance(self.cities[self.actual_tour[i]], self.cities[self.actual_tour[i + 1]]) 
                     for i in range(len(self.actual_tour) - 1)]
        calculated_max_distance = max(distances)
        self.assertAlmostEqual(calculated_max_distance, self.actual_max_distance, places=5)

if __name__ == '__main__':
    unittest.main()