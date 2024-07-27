import unittest
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        # City coordinates: city index: (x, y)
        self.city_coords = {
            0: (29, 51),
            1: (49, 20),
            2: (79, 69),
            3: (17, 20),
            4: (18, 61),
            5: (40, 57),
            6: (57, 30),
            7: (36, 12),
            8: (93, 43),
            9: (17, 36),
            10: (4, 60),
            11: (78, 82),
            12: (83, 96),
            13: (60, 50),
            14: (98, 1)
        }

        # Provided solution
        self.solution_tour = [0, 3, 1, 8, 13, 5, 0]
        self.reported_cost = 182.34414639983973

    def test_number_of_cities(self):
        # [Requirement 1]
        self.assertEqual(len(set(self.solution_tour)), 6, "The tour should include exactly 6 unique cities")
        
    def test_start_and_end_at_depot(self):
        # [Requirement 2]
        self.assertEqual(self.solution_tour[0], 0, "The tour should start at the depot (City 0)")
        self.assertEqual(self.solution_tour[-1], 0, "The tour should end at the depot (City 0)")

    def test_calculated_cost(self):
        # [Requirement 3]
        total_cost = 0
        for i in range(1, len(self.solution_tour)):
            city1 = self.solution_tour[i - 1]
            city2 = self.solution_tour[i]
            total_cost += calculate_distance(*self.city_coords[city1], *self.city_coords[city2])
        
        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="The reported total travel cost should match the calculated cost based on the city coordinates")

    def test_output_format(self):
        # [Requirement 4]
        is_list = isinstance(self.solution_tour, list)
        is_number = isinstance(self.reported_cost, (int, float))
        self.assertTrue(is_list and is_number, "Output should be a list of city indices and a numeric total cost")

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTSPSolution))
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

main()