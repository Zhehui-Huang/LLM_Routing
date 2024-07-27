import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        # Given city coordinates as per the problem statement
        self.coordinates = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
                            (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
                            (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]
        self.tour_given = [0, 12, 8, 7, 6, 13, 2, 3, 16, 11, 17, 5, 15, 0]
        self.cost_given = 434.757445258872

    def calculate_distance(self, city1, city2):
        # Calculate Euclidean distance between two cities
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def test_tour_starts_and_ends_at_depot(self):
        # Test whether the tour starts and ends at the depot city
        self.assertEqual(self.tour_given[0], 0)
        self.assertEqual(self.tour_given[-1], 0)

    def test_tour_length(self):
        # Test whether the tour visits exactly 13 cities including the depot
        self.assertEqual(len(set(self.tour_given)), 13)

    def test_total_travel_cost(self):
        # Calculate the total tour cost and compare with the given total travel cost
        calculated_cost = sum(self.calculate_distance(self.tour_given[i], self.tour_given[i + 1]) 
                              for i in range(len(self.tour_given) - 1))
        self.assertAlmostEqual(calculated_instance_cost, self.cost_given, places=5)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)