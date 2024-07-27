import unittest
import math

# Define the coordinates of the cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# The provided tour and its total cost
provided_tour = [0, 9, 7, 14, 12, 0]
provided_cost = 279.26

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their IDs."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total_cost

class TestTourSolution(unittest.TestCase):
    
    def test_tour_starts_and_ends_at_depot(self):
        """Test that the tour starts and ends at the depot city."""
        self.assertEqual(provided_tour[0], 0)
        self.assertEqual(provided_tour[-1], 0)
    
    def test_tour_length(self):
        """Test that exactly 6 cities are visited in the tour."""
        self.assertEqual(len(set(provided_tour)), 6)
    
    def test_tour_cost(self):
        """Test that the provided total travel cost matches the actual calculated cost."""
        calculated_cost = calculate_total_tour_cost(proached_tour)
        self.assertAlmostEqual(calculated_cost, provided_cost, places=2)
    
    def test_tour_contains_valid_cities(self):
        """Test that all cities in the tour are valid (i.e., within the range of defined cities)."""
        for city in provided_tour:
            self.assertIn(city, cities)
    
    def test_tour_completes_requirement(self):
        """Simulate full tour and check final assessment."""
        if (self.test_tour_starts_and_ends_at_depot() and
            self.test_tour_length() and
            self.test_tour_cost() and
            self.test_tour_contains_valid_cies()):
            return "CORRECT"
        else:
  onHistionisteng aandor"""       
  rFAILED

# Run the test
unittest.main(argv=[''], verbosity=2, exit=False)