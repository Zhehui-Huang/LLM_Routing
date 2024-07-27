import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    # Start and end check
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at the depot city 0."

    # Visit all cities exactly once, except the depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return False, "Tour must visit all cities exactly once, returning to the depot."

    # Verify distances
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    return True, total_distance

class TestRobotTour(unittest.TestCase):
    def test_robot_tour(self):
        cities = [
            (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
            (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
            (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
        ]

        # Provided solution
        solution_tour = [0, 13, 10, 8, 14, 3, 6, 11, 12, 4, 7, 2, 5, 9, 1, 0]
        solution_cost = 324.91232585922467

        # Check tour validity and calculate the travel cost
        valid, calculated_cost = verify_tour(solution_tour, cities)

        # Check requirements for correctness
        self.assertTrue(valid, "Tour constraints not met.")
        self.assertAlmostEqual(calculated_cost, solution_cost, places=5, 
                               msg=f"Calculated cost {calculated_cost} does not match provided solution cost {solution_cost}.")

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    test_result = unittest.TextTestRunner().run(test_suite)

    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")