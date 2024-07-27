import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Coordinates of cities
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        # Proposed tour and its cost
        self.tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        self.tour_cost = 315.5597914831042
    
    def test_cities_count(self):
        # Test the count of cities listed
        self.assertEqual(len(self.cities), 10, "There should be 10 cities including the depot.")
    
    def test_start_end_at_depot(self):
        # Tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city (0).")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city (0).")
    
    def test_visits_all_cities_exactly_once(self):
        # All cities visited exactly once except the depot
        city_counts = {city: self.tour.count(city) for city in range(10)}
        city_counts[0] -= 2  # Adjust for the start and end at the depot
        self.assertTrue(all(count == 1 for count in city_counts.values()), "Each city should be visited exactly once.")
    
    def test_tour_distance_calculation(self):
        # Check the calculated distance with the Euclidean formula
        def distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        total_cost_computed = 0
        for i in range(len(self.tour) - 1):
            total_cost_computed += distance(self.tour[i], self.tour[i + 1])
        
        self.assertAlmostEqual(self.tour_cost, total_cost_computed, places=5, msg="Calculated travel cost should be accurate.")
    
    def test_output_tour_and_cost(self):
        # Validate that the tour and tour cost are as expected
        correct_tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
        correct_cost = 315.5597914831042
        self.assertEqual(correct_tour, self.tour, "Tour order should be correct.")
        self.assertAlmostEqual(correct_cost, self.tour_cost, places=5, msg="Calculated cost should be correct.")

# Execute the tests
if __name__ == '__main__':
    unittest.main()