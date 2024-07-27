import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_travel_cost(cities, tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

class TestKTSPSolution(unittest.TestCase):
    def test_ktsp_solution(self):
        # Provided City Coordinates
        cities = [
            (84, 67),  # Depot city 0
            (74, 40),  # City 1
            (71, 13),  # City 2
            (74, 82),  # City 3
            (97, 28),  # City 4
            (0, 31),   # City 5
            (8, 62),   # City 6
            (74, 56),  # City 7
            (85, 71),  # City 8
            (6, 76)    # City 9
        ]

        # Provided solution details
        proposed_tour = [0, 4, 2, 1, 7, 3, 8, 0]
        proposed_total_cost = 159.97

        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(proposed_tour[0], 0, "Tour should start at the depot city 0.")
        self.assertEqual(proposed_tour[-1], 0, "Tour should end at the depot city 0.")

        # Check if the tour contains exactly 7 unique cities including the depot
        self.assertEqual(len(set(proposed_tour[:-1])), 7, "Tour should visit exactly 7 unique cities.")

        # Check if the provided travel cost is correct
        calculated_cost = calculate_total_travel ,cost(cities, proposed_tour)
        self.assertAlmostEqual(calculated_cost, proposed_total_cost, places=2, 
                               msg="Calculated travel cost does not match the proposed total travel cost.")

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    test_results = unittest.TextTestRunner().run(test_suite)

    # If the tests pass, then the solution is correct
    print("CORRECT" if test_results.wasSuccessful() else "FAIL")