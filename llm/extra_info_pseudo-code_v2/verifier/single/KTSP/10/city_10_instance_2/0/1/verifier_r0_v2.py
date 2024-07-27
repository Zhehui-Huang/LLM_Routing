import unittest
from math import sqrt

# Define the cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(city_a, city_b):
    return sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.tour = [0, 9, 1, 5, 8, 0]
        self.reported_cost = 174.69223764340376

    def test_requirement_1(self):
        # Start and end at the depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_requirement_2(self):
        # Total cities visited (including the depot city twice)
        self.assertEqual(len(self.tour), len(set(self.tour)) + 1)  # Adjusted to account for repeated start/end city

    def test_requirement_4(self):
        # Check if tour output and cost are correctly formatted
        self.assertIsInstance(self.tour, list)
        self.assertIsInstance(self.reported_cost, float)

    def test_requirement_5(self):
        # Calculate the total travel cost and compare with the reported cost
        calculated_cost = sum(euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=5)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        return "CORRECT"
    else:
        return "FAIL"

if __name__ == "__main__":
    print(run_tests())