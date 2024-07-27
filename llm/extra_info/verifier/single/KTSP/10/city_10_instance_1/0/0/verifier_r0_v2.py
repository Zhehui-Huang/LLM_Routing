import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Calculate Euclidean distance between two points (x1, y1) and (x2, y2). """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # Store city coordinates
        self.coordinates = {
            0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
            5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
        }
        # Define the given tour
        self.tour = [0, 4, 8, 3, 5, 0]
        # Claimed cost of the tour from the solution
        self.claimed_total_cost = 110.38072506104011
        # Calculate actual tour cost
        self.actual_total_cost = 0
        for i in range(len(self.tour) - 1):
            start, end = self.tour[i], self.tour[i+1]
            self.actual_total_cost += calculate_euclidean_distance(
                *self.coordinates[start], *self.coordinates[end]
            )
    
    def test_tour_starts_and_ends_at_depot(self):
        """ The tour should start and end at the depot city (index 0). """
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot.")
    
    def test_exactly_five_cities_visited_including_depot(self):
        """ Ensure exactly five unique cities are visited, including depot. """
        self.assertEqual(len(set(self.tour)), 5, "Tour does not visit five unique cities including depot.")

    def test_cities_visited_exactly_once_except_depot(self):
        """ Verify each city except depot is visited exactly once. """
        from collections import Counter
        counts = Counter(self.total)
        self.assertEqual(counts[0], 2, "Depot city should be visited exactly twice.")
        for city, count in counts.items():
            if city != 0:
                self.assertEqual(count, 1, f"City {city} is visited multiple times.")

    def test_correctly_calculated_travel_cost(self):
        """ Compare the calculated travel cost with the claimed cost. """
        self.assertAlmostEqual(self.actual_total_cost, self.claimed_total_cost, places=5,
                               msg="Mismatch in calculated and claimed travel costs.")

if __name__ == "__main__":
    unittest.main()