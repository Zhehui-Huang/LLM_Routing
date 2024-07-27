import unittest
from math import sqrt

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Groups
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

class TestSolution(unittest.TestCase):
    def test_requirements(self):
        # Tour and total travel cost given
        tour = [0, 10, 1, 9, 0]
        reported_cost = 122.22

        # [Requirement 1]
        # Check if tour starts and ends at the depot
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

        # [Requirement 2]
        # Check if exactly one city from each group is visited
        visited_groups = {g: 0 for g in range(len(groups))}
        unique_cities = set(tour)
        unique_cities.remove(0)  # Remove the depot city
        for city in unique_cities:
            for i, group in enumerate(groups):
                if city in group:
                    visited_groups[i] += 1
        self.assertTrue(all(count == 1 for count in visited_groups.values()))

        # [Requirement 3]
        # Check if the total distance is correctly calculated
        calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        # Allow a small margin of error for float comparisons
        self.assertAlmostEqual(calculated_cost, reported_cost, places=2)

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    all_tests_passed = (len(test_results.errors) == 0 and len(test_results.failures) == 0)
    print("CORRECT" if all_tests_passed else "FAIL")