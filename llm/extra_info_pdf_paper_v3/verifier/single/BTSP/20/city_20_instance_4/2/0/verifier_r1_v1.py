import unittest
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Class for unit testing
class TestTSPSolution(unittest.TestCase):
    def test_tsp_solution(self):
        # Coordinates of cities
        cities = {
            0: (26, 60),
            1: (73, 84),
            2: (89, 36),
            5: (69, 22),
            3: (15, 0),
            4: (11, 10)
        }

        # Provided solution
        tour = [0, 1, 2, 5, 3, 4, 0]
        expected_max_distance = 58.309518948453004
        provided_total_cost = 249.0640341092713

        # Check if tour starts and ends at the depot city 0
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # Check if each city is visited exactly once
        self.assertEqual(len(set(tour[:-1])), 6)  # Each city from 0 to 5 is in the set, excluding the last 0

        # Check total travel cost and max distance
        calculated_total_cost = 0
        distances = []

        for i in range(len(tour) - 1):
            distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
            distances.append(distance)
            calculated_total_cost += distance

        calculated_max_distance = max(distances)

        # Check values
        self.assertAlmostEqual(calculated_total_cost, provided_total_cost, places=6)
        self.assertAlmostEqual(calculated_max_distance, expected_max_distance, places=6)

# Execute the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)