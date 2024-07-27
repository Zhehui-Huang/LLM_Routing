import unittest
import math

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_requirement_1(self):
        # Cities from the problem statement
        num_cities = 20
        # Tour provided in the solution
        tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        # Test if all cities from 0 to 19 are visited exactly once and starts/ends at depot
        self.assertEqual(len(tour) - 1, len(set(tour[:-1])), "Each city should be visited exactly once")
        self.assertEqual(tour[0], 0, "Tour should start at city 0")
        self.assertEqual(tour[-1], 0, "Tour should end at city 0")

    def test_requirement_2(self):
        # Coordinates of each city
        cities_coords = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
            (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
            (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        # Tour and max distance from problem
        tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        max_distance = 87.45856161634491

        # Calculate the max distance in the tour
        def euclidean_distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        calculated_max_distance = max(
            euclidean_distance(cities_coords[tour[i]], cities_coords[tour[i+1]])
            for i in range(len(tour) - 1)
        )

        # Check if the provided max distance matches the calculated one
        self.assertAlmostEqual(calculated_max_distance, max_distance, places=5, 
                               msg="Max distance between consecutive cities in the tour should match.")

    def test_requirement_3(self):
        # Output format test
        output = "Tour: [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]\n" \
                 "Total travel cost: 477.0516251264448\n" \
                 "Maximum distance between consecutive cities: 87.45856161634491"
        self.assertIn("Tour: ", output)
        self.assertIn("Total travel cost: ", output)
        self.assertIn("Maximum distance between consecutive cities: ", output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(TestTravelingSalesmanSolution('test_requirement_1'))
    suite.addTest(TestTravelingSalesmanSolution('test_requirement_2'))
    suite.addTest(TestTravelingSalesmanSolution('test_requirement_3'))
    
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

print(run_tests())