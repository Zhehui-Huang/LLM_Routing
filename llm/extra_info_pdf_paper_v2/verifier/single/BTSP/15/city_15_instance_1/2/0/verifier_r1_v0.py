import unittest
from math import sqrt

# Coordinates of the cities
cities = [
    (29, 51),  # City 0: Depot
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

solution_data = {
    'Tour': [0, 4, 10, 5, 9, 3, 7, 1, 6, 13, 2, 8, 14, 11, 12, 0],
    'Total travel cost': 448.3684060133047,
    'Maximum distance between consecutive cities': 83.43260753446461
}

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities given their coordinates. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

class TestSolution(unittest.TestCase):
    def test_tour_start_end_depot(self):
        """ Test if the tour starts and ends at the depot city. """
        tour = solution_data['Tour']
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_all_cities_visited_once(self):
        """ Test if all cities are visited exactly once, apart from the depot city which is visited twice (start and end). """
        tour = solution_data['Tour']
        for city in range(1, 15):
            self.assertEqual(tour.count(city), 1)

    def test_minimize_longest_distance(self):
        """ Test if the longest distance between any two consecutive cities is as specified. """
        tour = solution_tour = solution_data['Tour']
        max_distance = max(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        self.assertAlmostEqual(max_distance, solution_data['Maximum distance between consecutive cities'])

# Running the tests
if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    test_results = unittest.TextTestRunner().run(test_suite)
    output_result = "CORRECT" if test_results.wasSuccessful() else "FAIL"
    print(output_result)