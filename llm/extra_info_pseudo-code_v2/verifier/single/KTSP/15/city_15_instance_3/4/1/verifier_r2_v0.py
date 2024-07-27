import unittest
from math import sqrt

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):

    def setUp(self):
        # Given city coordinates including depot city
        self.cities = [
            (16, 90),  # Depot city 0
            (43, 99),  # City 1
            (80, 21),  # City 2
            (86, 92),  # City 3
            (54, 93),  # City 4
            (34, 73),  # City 5
            (6, 61),   # City 6
            (86, 69),  # City 7
            (30, 50),  # City 8
            (35, 73),  # City 9
            (42, 64),  # City 10
            (64, 30),  # City 11
            (70, 95),  # City 12
            (29, 64),  # City 13
            (32, 79)   # City 14
        ]

        # Provided tour and cost
        self.tour = [0, 1, 12, 3, 7, 9, 5, 13, 8, 6, 0]
        self.calculated_cost = self.calculate_total_travel_cost()

    def calculate_total_travel_discounted_cost(self):
        # Given tour with cost 228.598
        return 228.598

    def calculate_total_travel_cost(self):
        cost = 0
        for i in range(len(self.tour) - 1):
            cost += euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        return cost

    def test_tour_length_and_start_end(self):
        self.assertEqual(len(self.tour), 11)  # 10 cities + returning to depot
        self.assertEqual(self.tour[0], self.tour[-1], "Tour must start and end at the depot city")

    def test_unique_cities(self):
        # each city except depot should be visited exactly once
        unique_cities = set(self.tour)
        self.assertTrue(all(self.tour.count(city) == 1 for city in unique_cities - {0}))

    def test_travel_cost(self):
        expected_cost = self.calculate_total_travel_discounted_cost()
        self.assertAlmostEqual(self.calculated_cost, expected_cost, places=2, msg="Calculated travel cost is incorrect")

    def runTest(self):
        self.test_tour_length_and_start_end()
        self.test_unique_cities()
        self.test_travel_cost()

# Running the test
test_suite = unittest.TestSuite()
test_suite.addTest(TestRobotTour())
runner = unittest.TextTestRunner()

results = runner.run(test_suite)
if len(results.failures) == 0:
    print("CORRECT")
else:
    print("FAIL")