import unittest
from math import sqrt

# City coordinates from the problem statement
cities = {
    0: (8, 11),
    3: (80, 60),
    11: (40, 87),
    16: (13, 43)
}

def calculate_distance(c1_idx, c2_idx):
    """ Calculate the Euclidean distance between two cities given their indices. """
    c1, c2 = cities[c1_idx], cities[c2_idx]
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Solution provided
        self.tour = [0, 3, 11, 16, 0]
        self.total_cost_reported = 219.36

    def test_tour_start_and_end_city(self):
        """ Tour should start and end at the depot city, city 0. """
        self.assertEqual(self.tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at city 0")

    def test_tour_length(self):
        """ The robot has to visit exactly 4 unique cities, including the depot city. """
        self.assertEqual(len(set(self.tour)), 4, "Tour does not contain exactly 4 unique cities including the depot.")

    def test_tour_representation(self):
        """ Tour path should be represented as a list of city indices, all indexed correctly. """
        correct_indices = all(city in cities.keys() for city in set(self.tour))
        self.assertTrue(correct_indices, "Tour contains invalid city indices")

    def test_total_travel_cost(self):
        """ Check if the computed total travel cost mathces the reported cost. """
        actual_cost = round(sum(calculate_distance(self.tour[i], self.tour[i + 1])
                          for i in range(len(self.tour) - 1)), 2)
        self.assertAlmostEqual(self.total_cost_reported, actual_cost, places=2, msg="Reported total travel cost is incorrect")

# Run the test suite
if __name__ == '__main__':
    unittest.main()