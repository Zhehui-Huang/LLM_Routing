import unittest
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
            (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
            (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
            (51, 58), (30, 48)
        ]
        self.tour = [0, 12, 0]
        self.total_travel_cost = 28.844410203711913
        self.max_distance_between_cities = 14.422205101855956

    def test_visit_each_city_once(self):
        # Ensure all cities except depot are visited exactly once
        self.assertCountEqual(self.tour[1:-1], list(range(1, len(self.cities))))

    def test_start_end_depot(self):
        # Start and end at depot
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_euclidean_distance_as_travel_cost(self):
        # Compute distances and total travel cost
        computed_total_cost = 0
        computed_max_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.cities[self.tour[i]]
            city2 = self.cities[self.tour[i + 1]]
            distance = euclidean_distance(city1, city2)
            computed_total_cost += distance
            computed_max_distance = max(computed_max_distance, distance)

        # Check the total cost and max distance
        self.assertAlmostEqual(computed_total_cost, self.total_travel_cost)
        self.assertAlmostEqual(computed_max_distance, self.max_distance_between_cities)

if __name__ == '__main__':
    # Run the unit tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")