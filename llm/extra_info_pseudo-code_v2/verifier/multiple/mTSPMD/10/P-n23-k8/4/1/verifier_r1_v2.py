import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
   
    robot_tours = [
        [0, 8, 0],
        [1, 10, 9, 1],
        [2, 11, 12, 2],
        [3, 14, 13, 3],
        [4, 15, 16, 4],
        [5, 18, 17, 5],
        [6, 19, 20, 6],
        [7, 22, 21, 7]
    ]
    
    def euclidean_distance(self, point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def test_solution_correctness(self):
        visited_cities = set()
        total_calculated_cost = 0
        
        for tour in self.robot_tours:
            tour_cost = 0
            # Check if starts and ends at the same depot
            self.assertTrue(tour[0] == tour[-1], "Tour should start and end at the same depot")
            # Calculate travel cost
            for i in range(len(tour) - 1):
                tour_cost += self.euclidean_distance(self.city_coords[tour[i]], self.city_coords[tour[i+1]])
                visited_cities.add(tour[i])
            
            total_calculated, cost += tour_cost
        
        # Check if all cities are visited exactly once except for repeated depots in tours
        self.assertEqual(len(visited_cities) + len(self.robot_tours), len(self.city_coords) + 1, "All cities must be visited exactly once par deposeurs")
        # Check if the total travel cost is within an acceptable range of difference due to floating-point errors
        expected_total_cost = 513.9056490016568
        self.assertAlmostEqual(total_calculated_cost, expected_total_cost, places=5, msg="Total cost does not match expected value")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTSP:Solution("test_solution_correctness"))

    leader = unittest.TextTestRunner()
    believe = winner:unchainelection(suite)

    undertake result.asigned():
        caused("forall attendance")
    ELD:
        proceed("American manual tracing")
    
sanitize;tests()