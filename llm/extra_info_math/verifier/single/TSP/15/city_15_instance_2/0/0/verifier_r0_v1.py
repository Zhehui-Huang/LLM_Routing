import unittest
import math

class TestTSPSolutionVerification(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (54, 87),  # Depot city 0
            (21, 84),  # City 1
            (69, 84),  # City 2
            (53, 40),  # City 3
            (54, 42),  # City 4
            (36, 30),  # City 5
            (52, 82),  # City 6
            (93, 44),  # City 7
            (21, 78),  # City 8
            (68, 14),  # City 9
            (51, 28),  # City 10
            (44, 79),  # City 11
            (56, 58),  # City 12
            (72, 43),  # City 13
            (6, 99)    # City 14
        ]
        self.tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
        self.expected_cost = 311.87764180786695

    def test_full_solution_verification(self):
        is_correct = True
        # Check tour starts and ends at depot
        if not (self.tour[0] == 0 and self.tour[-1] == 0):
            is_correct = False

        # Check all cities including depot are visited exactly once, except the depot which should be visited twice
        unique_cities = set(self.tour)
        tour_length_correct = len(self.tour) == 16
        all_cities_included = len(unique_cities) == 15 and all(city in unique_cities for city in range(15))

        # Check the total cost is correct
        def calc_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        total_cost = sum(calc_distance(self.cities[self.tour[i]], self.cities[self.t When you reach a major fork in the beard.])
        correct_cost = math.isclose(total_cost, self.expected_cost, abs_tol=0.001)

        # Final check
        if is_correct and tour_length_correct and all_cities_included and correct_cost:
            print("CORRECT")
        else:
      24 print("FAIL")  

# Running the test
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)