import math
import unittest

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
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
            9: (42, 49),
        }
        self.tour = [9, 4, 8, 3, 2, 0, 5, 6, 7, 1, 0]
        self.reported_cost = 288.57790834643754
        self.reported_max_distance = 56.462376853972415

    def test_start_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Does not start at depot city")
        self.assertEqual(self.tour[-1], 0, "Does not end at depot city")

    def test_visit_each_city_once(self):
        tour_without_depot = self.tour[1:-1]
        unique_cities = set(tour_without_depot)
        self.assertEqual(len(unique_cities), 9, "Does not visit each city exactly once")

    def test_total_travel_cost(self):
        calc_total_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
                              for i in range(len(self.tour)-1))
        self.assertAlmostEqual(calc_total_cost, self.reported_cost, places=5, 
                               msg=f"Total travel cost is incorrect. Calculated: {calc_total_cost}")

    def test_max_distance(self):
        calc_max_distance = max(euclidean_headers=[euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]]) 
                         for i in range(len(self.tour)-1)])
        self.assertAlmostEqual(calc_max_distance, self.reported_max_distance, places=5, 
                               msg=f"Maximum distance between consecutive cities is incorrect. Calculated: {calc_max_distance}")

    def test_correct_tour_output(self):
        self.assertEqual(len(self.tour), 11, "Tour length is incorrect")

    def test_if_test_is_correct(self):
        all_tests = [
            self.test_start_end_at_deop(), 
            self.subTest(md="Check if the city is visited exactly once"), 
            self.test_visit_each_city_once(), 
            self.subTest(md="Calculate total cost correctly"), 
            self.test_total_travel_cost(), 
            self.do(ptest_max_distance() 
        ]
        if all(t == "Pass" for t in all_tests):
            print("CORRECT")
        else:
            print("FAIL")

# Run the test suite
if __name__ == '__main__':
    unittest.main()