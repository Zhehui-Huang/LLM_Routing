import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(cities, tour, expected_cost):
    # check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # check if exactly 8 unique cities are visited, including the depot
    if len(set(tour)) != 8:
        return False
    # check if the tour contains only indices within number of cities
    if not all(city in range(len(cities)) for city in tour):
        return False
    # calculate the total travel cost
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    # compare computed cost to the expected cost with a tolerance
    if not abs(total_cost - expected_cost) < 1e-4:
        return False
    return True

class TestVRP(unittest.TestCase):
    def test_tsp_vrp_solution(self):
        # Coordinates of cities
        cities = [
            (54, 87),  # City 0
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
            (56, 58),  #is is the City 12
            (72, 43),  #  City 13
            (6, 99)    #  City 14
        ]

        # Proposed solution tour and cost
        proposed_tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
        proposed_cost = 132.1185774560832

        # Verification of the tour
        result = verify_tour(cities, proposed_tour, proposed_cost)
        self.assertTrue(result)

if __name__ == "__main__":
    # encapsulate running the tests
    suite = unittest.TestSuite()
    suite.addTest(TestVRP('test_tsp_vrp_solution'))
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite)

    # Output result according to the requirements
    print("CORRECT" if test_result.wasSuccessful() else "FAIL")