import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def setUp(self):
        # Cities coordinates including the depot city
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        # Provided solution
        self.tour = [0, 4, 1, 7, 3, 8, 0]
        self.reported_cost = 128.73

    def test_tour_start_end_depot(self):
        # Check if the robot starts and ends at the depot city 0
        self.assertEqual(self.tour[0], 0, "Tour should start at depot city")
        self.assertEqual(self.tour[-1], 0, "Tour should end at depot city")

    def test_total_cities_visited(self):
        # Check total number of cities visited
        self.assertEqual(len(set(self.tour)), 7, "Number of unique cities visited should be 7 (including depot)")

    def test_travel_cost(self):
        # Calculate the travel cost from the tour and compare with given cost
        def euclidean_distance(coord1, coord2):
            return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
        
        calculated_cost = 0
        for i in range(len(self.tour) - 1):
            city_from = self.tour[i]
            city_to = self.tour[i + 1]
            calculated_cost += euclidean_distance(self.cities[city_from], self.cities[city_to])
        
        # Tolerance to handle floating point arithmetic issues        
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2,
                               msg="Calculated tour cost should roughly match the reported cost")

    def test_output_format(self):
        # Check list length (should be 7 unique + 1 repeated depot city at the end)
        self.assertEqual(len(self.tour), 7, "Tour length should be exactly 7 unique cities visited including repetitions")
        # Check if tour is outputted correctly
        self.assertIsInstance(self.tour, list, "Tour should be a list")
        self.assertIsInstance(self.reported_cost, float, "Cost should be a float")

# Running the tests
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestTravelingSalesmanSolution)
    test_result = unittest.TextTestRunner().run(test_suite)

    # Determine if the solution is correct based on the test results
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")