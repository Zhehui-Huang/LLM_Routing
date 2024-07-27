import unittest
import math

# Constants
CITIES = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_travel_cost(tour):
    return sum(euclidean_distance(CITIES[tour[i]], CITIES[tour[i+1]]) for i in range(len(tour) - 1))

class TestTourSolution(unittest.TestCase):
    def test_tour_validity(self):
        tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
        calculated_cost = round(total_travel_cost(tour), 2)

        # Check Requirement 1: Starts and ends at depot
        self.assertEqual(tour[0], 0, "Tour should start at depot city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at depot city 0")

        # Check Requirement 2: All cities visited exactly once
        unique_cities = list(set(tour[1:-1]))
        self.assertEqual(len(unique_cities), len(CITIES)-1, "All cities must be visited exactly once")
        self.assertCountEqual(unique_cities, range(1, len(CITIES)), "Tour must cover all cities exactly once")

        # Check Requirement 5: Correct total cost reported
        expected_cost = 278.93
        self.assertAlmostEqual(calculated_cost, expected_cost, places=2, msg="Total travel cost is incorrect")

# Run the tests
if __name__ == "__main__":
    unittest.main()