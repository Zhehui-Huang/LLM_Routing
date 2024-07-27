import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.positions = [
            (35, 40),  # Depot
            (39, 41),
            (81, 30),
            (5, 50),
            (72, 90),
            (54, 46),
            (8, 70),
            (97, 62),
            (14, 41),
            (70, 44),
            (27, 47),
            (41, 74),
            (53, 80),
            (21, 21),
            (12, 39)
        ]
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.reported_cost = 337.84
        self.tour_requirements_met = True

    def test_tour_start_end_at_depot(self):
        self.assertTrue(self.tour[0] == self.tour[-1] == 0, "Tour does not start and end at the depot")

    def test_all_cities_visited_exactly_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 14, "Not all cities are visited exactly once")

    def test_calculate_total_travel_cost(self):
        calculated_cost = self.calculate_total_distance(self.positions, self.tour)
        self.assertAlmostEqual(calculatedacet, self.reported_cost, places=2, "Calculated cost does not match reported cost")

    def calculate_distance(self, pos1, pos2):
        return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def calculate_total_distance(self, positions, tour):
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += self.calculate_distance(positions[tour[i]], positions[tour[i+1]])
        return total_distance

    def runTest(self):
        try:
            self.test_tour_start_end_at_depot()
            self.test_all_cities_visited_exactly_once()
            self.test_calculate_total_travel_cost()
        except AssertionError:
            self.tour_requirements_met = False

        if self.tour_requirements_met:
            print("CORRECT")
        else:
            print("FAIL")

# Run the test
test_suite = unittest.TestSuite()
test_case = TestRobotTour()
test_suite.addTest(test_case)
runner = unittest.TextTestRunner()
runner.run(test_suite)