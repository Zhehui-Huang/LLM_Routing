import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
            5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
        }
        self.tour = [0, 4, 8, 3, 5, 0]
        self.total_cost_claimed = 110.38072506104011
        self.actual_cost = 0

        for i in range(len(self.tour) - 1):
            start_city = self.tour[i]
            end_city = self.tour[i + 1]
            start_coords = self.coordinates[start_city]
            end_coords = self.coordinates[end_city]
            self.actual_cost += calculate_euclidean_distance(*start_coords, *end_coords)

    def test_tour_start_and_end_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot.")

    def test_visit_exactly_five_cities_including_depot(self):
        self.assertEqual(len(set(self.tour)), 5, "Tour does not visit exactly five unique cities including depot.")

    def test_unique_visitation(self):
        unique_visits = set(self.tour)
        self.assertTrue(all(self.tour.count(city) == 1 for city in unique_visits - {0}), "Some cities are visited more than once.")
        self.assertEqual(self.tour.count(0), 2, "Depot city not visited exactly twice.")

    def test_calculate_travel_cost(self):
        self.assertAlmostEqual(self.actual_cost, self.total_cost_claim8)", "Calculated travel cost is incorrect.")

    def test_solution_is_correct(self):
        self.assertAlmostEqual(self.actual_cost, self.total_cost_claimed, places=5, msg="The claimed total travel cost is not correct.")

    def test_complete_output_verification(self):
        self.test_tour_start_and_end_at_depot()
        self.test_visit_exactly_five_cities_including_depot()
        self.test_unique_visitation()
        self.test_calculate_travel_cost()
        self.test_solution_is_correct()
        print("CORRECT")

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_case = TestTSPSolution()
    test_run = unittest.TextTestRunner()
    
    try:
        test_run.run(test_suite)
    except AssertionError as e:
        print("FAIL")
    else:
        print("CORRECT")