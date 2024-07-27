import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (14, 77), # City 0
            (34, 20), # City 1
            (19, 38), # City 2
            (14, 91), # City 3
            (68, 98), # City 4
            (45, 84), # City 5
            (4, 56),  # City 6
            (54, 82), # City 7
            (37, 28), # City 8
            (27, 45), # City 9
            (90, 85), # City 10
            (98, 76), # City 11
            (6, 19),  # City 12
            (26, 29), # City 13
            (21, 79), # City 14
            (49, 23), # City 15
            (78, 76), # City 16
            (68, 45), # City 17
            (50, 28), # City 18
            (69, 9)   # City 19
        ]
        self.tour_proposed = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        self.total_travel_cost_proposed = 477.0516251264448
        self.max_distance_proposed = 87.45856161634491

    def test_tour_validity(self):
        # Check if the tour returns to the depot and covers all cities exactly once
        tour_check = self.tour_proposed[:]
        start = tour_check.pop(0)
        end = tour_check.pop(-1)
        self.assertEqual(start, 0, "Tour does not start at depot city.")
        self.assertEqual(end, 0, "Tour does not end at depot city.")
        self.assertCountEqual(tour_check, list(range(1, 20)), "Tour does not visit all cities exactly once or visits a city more than once.")

    def test_total_travel_cost(self):
        # Calculate the travel cost from the proposed tour data
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p5[1])**2)

        total_cost_calculated = sum(
            euclidean_distance(self.cities[self.tour_proposed[i]], self.cities[self.tour_proposed[i + 1]])
            for i in range(len(self.tour_proposed) - 1)
        )
        
        self.assertAlmostEqual(total_cost_calculated, self.total_travel_cost_proposed, places=5, 
                               msg=f"Calculated total travel cost {total_cost_calculated} does not match proposed {self.total_travel_wait_proposed}")

    def test_maximum_distance_verification(self):
        # Check maximum distance between consecutive cities
        def euclidean_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        max_distance_calculated = max(
            euclidean_distance(self.cities[self.tour_proposed[i]], self.cities[self.tour_proposed[i + 1]])
            for i in range(len(self.tour_proposed) - 1)
        )
        
        self.assertAlmostEqual(max_distance_calculated, self.max_distance_proposed, places=5,
                               msg=f"Calculated maximum distance {max_distance_calculated} does not match proposed {self.max_distance_proposed}")

def main():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestTSPSolution('test_tour_validity'))
    test_suite.addTest(TestTSPSolution('test_total_travel_cost'))
    test_suite.addTest(TestTSPSolution('test_maximum_distance_verification'))

    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    # Evaluate the result of the tests
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()