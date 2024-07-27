import math
from unittest import TestCase, main

class TestTSPSolution(TestCase):
    # Define the cities as points with coordinates
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Proposed solution
    tour = [0, 6, 7, 1, 5, 9, 4, 8, 3, 2, 0]
    total_travel_cost = 259.91

    def test_starts_and_ends_at_depot(self):
        # Requirement 1
        self.assertEqual(self.tour[0], 0, "Must start at the depot city.")
        self.assertEqual(self.tour[-1], 0, "Must return to the depot city.")

    def test_visits_all_cities_exactly_once(self):
        # Requirement 2
        # Check that each city except depot is visited exactly once
        unique_cities = set(self.tour[1:-1]) # Ignore the start/end depot in count
        all_cities = set(self.cities.keys()) - {0} # All cities except the depot
        self.assertSetEqual(unique_cities, all_cities, "Must visit all cities exactly once.")

    def test_travel_cost_computation(self):
        # Requirement 3
        calculated_cost = 0
        for i in range(1, len(self.tour)):
            start = self.cities[self.tour[i-1]]
            end = self.cities[self.tour[i]]
            calculated_cost += math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        self.assertAlmostEqual(self.total_travel_cost, round(calculated_cost, 2), places=2, msg="Cost calculation error.")

    def test_output_format(self):
        # Requirement 4 and 5
        self.assertIsInstance(self.tour, list, "Tour output must be a list.")
        self.assertIsInstance(self.total_travel_cost, float, "Total travel cost must be a float value.")
        
    def test_correct_solution(self):
        # Combined test to check all requirements and output the final correctness statement.
        try:
            self.test_starts_and_ends_at_depot()
            self.test_visits_all_cities_exactly_once()
            self.test_travel_cost_computation()
            self.test_output_format()
            print("CORRECT")
        except AssertionError:
            print("FAIL")

# Run tests
if __name__ == '__main__':
    main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)