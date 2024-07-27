import unittest
from math import sqrt

class TestSolutionValidation(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.cost = 337.8447016788252
        self.tour_positions = {
            0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
            5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
            10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
        }
    
    def test_tour_start_and_end_at_depot(self):
        # Requirement 1: Tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0, "Tour does not start at city 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at city 0")
        
    def test_tour_visits_all_cities_once(self):
        # Requirement 2: Visit all other cities exactly once
        from collections import Counter
        city_count = Counter(self.tour)
        self.assertEqual(city_count[0], 2, "Depot city must be visited exactly twice")
        self.assertTrue(all(city_count[city] == 1 for city in range(1, 15)), "All cities must be visited exactly once")
        
    def test_tour_distance_calculation(self):
        # Requirement 3: Check Euclidean distance calculation
        def calculate_distance(pos1, pos2):
            return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
        calc_cost = 0
        for i in range(len(self.tour) - 1):
            calc_cost += calculate_distance(self.tour_positions[self.tour[i]], self.tour_positions[self.tour[i+1]])
        self.assertAlmostEqual(calc_cost, self.cost, places=4, msg="Calculated travel cost doesn't match the given tour cost")
        
    def test_output_format(self):
        # Requirement 4: Check format of the tour output
        self.assertIsInstance(self.tour, list, "Tour output is not a list")
        self.assertIsInstance(self.tour[0], int, "City indices in tour are not integers")
        
        # Requirement 5: Check output format of cost
        self.assertIsInstance(self.cost, float, "Tour cost is not expressed as a float")
        
    def test_complete_validation(self):
        self.test_tour_start_and_end_at_depot()
        self.test_tour_visits_all_cities_once()
        self.test_tour_distance_calculation()
        self.test_output_format()
        print("CORRECT")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionValidation)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")