import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.tour = [0, 9, 5, 6, 0]
        self.reported_cost = 61.66  # This is the provided total travel cost

    def test_start_and_end_at_depot(self):
        # Check if the tour starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot")

    def test_exactly_four_cities_including_depot(self):
        # Check if exactly four different cities are visited, including the depot
        self.assertEqual(len(set(self.tour)), 4, "Tour does not visit exactly 4 cities including depot")

    def test_correct_calculation_of_travel_cost(self):
        # Function to calculate Euclidean distance
        def euclidean_distance(city1, city2):
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Compute total travel cost along the tour
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += euclidean_distance(self.tour[i], self.tour[i + 1])

        # Compare calculated cost against reported cost
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, msg="Calculated travel cost does not match reported")

    def test_output_format(self):
        # Check if output format is correct for tour
        self.assertIsInstance(self.tour, list, "Tour is not a list")
        self.assertTrue(all(isinstance(city, int) for city in self.tour), "Tour does not consist of integers")
        
        # Check if output format is correct for cost
        self.assertIsInstance(self.reported_cost, float, "Reported cost is not a float")

    def runTest(self):
        try:
            self.test_start_and_end_at_depot()
            self.test_exactly_four_cities_including_depot()
            self.test_correct_calculation_of_travel_cost()
            self.test_output_format()
            print("CORRECT")
        except AssertionError as e:
            print("FAIL:", e)

# Run the tests manually
test_suite = unittest.TestSuite()
test_suite.addTest(TestKTSPSolution())
runner = unittest.TextTestRunner()
runner.run(test_suite)