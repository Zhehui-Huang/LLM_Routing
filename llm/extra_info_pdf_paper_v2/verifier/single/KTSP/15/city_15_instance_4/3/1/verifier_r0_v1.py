import unittest
from math import sqrt

class TestOptimalTour(unittest.TestCase):
    
    def setUp(self):
        # City coordinates provided in the task
        self.coordinates = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]

        # Tour and cost claimed to be the solution
        self.proposed_tour = [0, 1, 5, 9, 7, 4, 12, 11, 3, 14, 8, 10, 0]
        self.proposed_cost = 225.01

    def test_tour_start_end_at_depot(self):
        # Check the start and end at the depot city
        self.assertEqual(self.proposed_tour[0], 0, "Tour does not start at the depot city.")
        self.assertEqual(self.proposed_tour[-1], 0, "Tour does not end at the depot city.")

    def test_visit_exactly_12_cities(self):
        # Check that 12 cities (including the depot) are visited
        self.assertEqual(len(set(self.proposed_tour)), 12, "The tour does not visit exactly 12 cities.")

    def test_only_valid_cities_in_tour(self):
        # Check that only cities from the given set are included
        self.assertTrue(all(city in range(15) for city in self.proposed_tour), "The tour contains invalid cities.")

    def test_travel_cost_calculation(self):
        # Calculate the actual travel cost
        def euclidean_distance(city1, city2):
            return sqrt((self.coordinates[city1][0] - self.coordinates[city2][0])**2 + (self.coordinates[city1][1] - self.coordinates[city2][1])**2)

        actual_cost = sum(euclidean_distance(self.proposed_tour[i], self.proposed_tour[i + 1]) for i in range(len(self.proposed_tour) - 1))
        
        # Check the travel cost calculation
        self.assertAlmostEqual(actual_cost, self.proposed_cost, places=2, msg="The reported travel cost is not accurately calculated.")
        
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOptimalTour)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_tests()