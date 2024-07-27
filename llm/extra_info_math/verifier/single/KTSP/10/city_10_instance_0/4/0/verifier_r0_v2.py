import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.cities = {
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
        self.tour = [0, 9, 5, 6, 0]
        self.reported_cost = 61.66

    def test_tour_validation(self):
        # Check if the tour includes exactly 4 cities plus return to depot
        valid_length = len(self.tour) == 5
        # Check if the tour starts and ends at the depot city
        valid_start_end = self.tour[0] == 0 and self.tour[-1] == 0
        # Calculate the total travel cost
        total_cost = 0
        for i in range(len(self.tour) - 1):
            total_cost += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        # Check if the calculated total cost is close to the reported cost
        valid_cost = abs(total_cost - self.report new_cost) < 0.01

        # Assert all conditions are true
        self.assertTrue(valid_length and valid_start_end and valid_cost)

# Function to run the test suite and output the result based on assertions.
def run_robot_tour_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_tour_validation'))
    
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)
    
    # Print result based on the test outcome
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

run_robot_tour_tests()