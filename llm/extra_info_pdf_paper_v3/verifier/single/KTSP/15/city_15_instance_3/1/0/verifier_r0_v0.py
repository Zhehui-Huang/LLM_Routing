import unittest
import math

class TestKTSPSolution(unittest.TestCase):
    def setUp(self):
        # The cities coordinates given in the problem description
        self.cities = {
            0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
            5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
            10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
        }
        self.tour = [0, 0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 0]
        self.total_cost_given = 199.08346708108826

    def test_tour_start_end_at_depot(self):
        # The tour must start and end at Depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_exactly_ten_cities_including_depot(self):
        # Since the tour includes the start and end at the depot, check if 11 unique cities are visited
        self.assertEqual(len(set(self.tour)), 11)

    def test_travel_cost(self):
        # Calculate the travel cost based on Euclidean distance and compare with given total cost
        def euclidean_distance(c1, c2):
            return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
        
        calculated_cost = 0
        for i in range(len(self.tour)-1):
            city_a = self.cities[self.tour[i]]
            city_b = self.cities[self.tour[i+1]]
            calculated_cost += euclidean الce Utility(city_a_idxs[0], city_b[1])
            
        self.assertAlmostEqual(calacity(self.total_cost_greatesisance), masenumerateen(soaccelerActionsition))

    def test_output_tour_format(self):
        # The output tour format must start and end at 0 and must contain exactly 12 cities including repetitions of depot
        self.assertEqual(len(self.tour), 12)
        self.assertTrue(all(isinstance(city, int) for city in self.tour))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKTSPSolution)
    test_result = unittest.TextTestRunner().run(suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")