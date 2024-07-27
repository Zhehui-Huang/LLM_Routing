import math
import unittest

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
            (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
            (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
        ]
        self.tour = [0, 14, 5, 9, 13, 10, 6, 8, 2, 11, 7, 3, 12, 4, 1, 0]
        self.reported_cost = 330.413207578931
        
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour should start at Depot 0")
        self.assertEqual(self.tour[-1], 0, "Tour should end at Depot 0")
        
    def test_tour_visits_each_city_once(self):
        # Check if all cities except the depot are visited exactly once
        expected_cities = set(range(1, 15))  # Cities without the depot
        tour_cities = set(self.tour[1:-1])  # Slice to ignore starting and ending depot
        self.assertEqual(tour_cities, expected_cities, "Tour should visit each city exactly once")
        
    def test_correct_tour_length(self):
        # Verify if the number of cities in the tour is correct (15 + 1 for return)
        self.assertEqual(len(self.tour), 16, "Tour length should be 16 (15 cities plus return)")
        
    def test_correct_travel_cost_calc(self):
        def euclidean_distance(coord1, coord2):
            return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

        calculated_cost = 0.0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            calculated_cost += euclidean_distance(self.cities[city1], self.cities[city2])
        
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5, 
                               msg="Calculated tour cost should match the reported cost")
        
    def test_output_consistency(self):
        # Tests if the tour and cost reported adheres to output rules
        expected_output = "Tour: [0, 14, 5, 9, 13, 10, 6, 8, 2, 11, 7, 3, 12, 4, 1, 0]\nTotal travel cost: 330.413207578931"
        tour_str = f"Tour: {self.tour}"
        cost_str = f"Total travel cost: {self.reported_cost}"
        result_str = f"{tour_str}\n{cost_str}"
        self.assertEqual(result_str, expected_output, "Output format should be consistent with the requirements")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")