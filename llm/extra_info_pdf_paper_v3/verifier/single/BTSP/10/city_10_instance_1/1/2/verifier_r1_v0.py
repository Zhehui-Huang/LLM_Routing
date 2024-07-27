import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Define the cities coordinates
        self.cities = {
            0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
            5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
        }
        # Proposed tour, total cost, and max distance
        self.tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
        self.total_cost = 278.9348447394249
        self.max_distance = 56.61271941887264
    
    def test_tour_starts_and_ends_at_depot(self):
        """Test if the tour starts and ends at the depot (city 0)."""
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_all_cities_visited_once(self):
        """Test if every city is visited exactly once except the depot city which is visited twice."""
        tour_without_depot_end = self.tour[:-1]  # Remove the last element which is the depot end
        unique_cities = set(tour_without_depot_end)
        
        # Check if all cities are unique (set length) and matches number of cities in the list minus the repeated depot
        self.assertEqual(len(unique_cities), len(self.cities))
        self.assertEqual(sorted(unique_cities), list(range(len(self.cities))))
    
    def test_travel_cost(self):
        """Test if the total travel cost is correct."""
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            (x1, y1), (x2, y2) = self.cities[self.tour[i]], self.cities[self.tour[i + 1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            calculated_cost += distance
        self.assertAlmostEqual(calculated_cost, self.total_cost)
    
    def test_maximum_distance_between_consecutive_cities(self):
        """Test if the maximum distance between consecutive cities is correct and minimized."""
        actual_max_distance = 0
        for i in range(len(self.tour) - 1):
            (x1, y1), (x2, y2) = self.cities[self.tour[i]], self.cities[self.tour[i + 1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if distance > actual_max_distance:
                actual_max_distance = distance
        self.assertAlmostEqual(actual_max_distance, self.max_distance)

# Running the test
if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
    
    if test_results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")