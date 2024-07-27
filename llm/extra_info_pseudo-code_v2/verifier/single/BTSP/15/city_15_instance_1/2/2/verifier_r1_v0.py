import unittest
import math

# List that represents the robot tour
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
# The provided maximum distance between any two consecutive cities in the tour
reported_max_distance = 85.21

# City coordinates
cities = [
    (29, 51),  # City 0 (Depot)
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    
    def test_tour_starts_and_ends_at_depot(self):
        # Check if the tour starts and ends at the depot (City 0)
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_visits_each_city_once(self):
        # Check if each city is visited exactly once (excluding the start/finish at depot)
        expected_cities = set(range(15))
        visited_cities = set(tour[1:-1])
        self.assertEqual(visited_cities, expected_cities)

    def test_maximum_distance_between_cities(self):
        # Calculate the maximum distance between consecutively visited cities in the tour
        max_distance = max(
            calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)
        )
        # Since the problem specifics to minimize this maximum distance,
        # we check if the reported max distance matches the calculated one
        self.assertAlmostEqual(max_distance, reported_max_distance, places=2)

# Run the tests
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestRobotTour))

runner = unittest.TextTestRunner()
result = runner.run(suite)

# Print overall result based on unit tests
if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")