import unittest
from math import sqrt

def euclidean_distance(city_a, city_b):
    return sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.total_travel_cost = float('inf')  # Given as inf

    def test_visit_all_cities_once_and_return(self):
        # Check if all cities except depot are visited exactly once and returns to depot
        visits = set(self.tour[1:-1])  # exclude the start and end depot
        self.assertEqual(visits, set(range(1, 10)))
        self.assertEqual(self.tour[0], self.tour[-1])  # starts and ends at depot

    def test_start_and_end_at_depot(self):
        # Check if tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_euclidean_distance_used(self):
        # Calculate the total travel cost using Euclidean distance and check with given cost
        calculated_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
                               for i in range(len(self.tour) - 1))
        if calculated_cost != float('inf'):
            self.assertAlmostEqual(calculated_cost, self.total_travel_cost)
        else:
            self.assertEqual(calculated_cost, self.total_travel_cost)

    def test_output_tour_and_cost(self):
        # Check if the total travel cost is correctly outputted
        expected_cost = float('inf')
        self.assertEqual(self.total_travel_cost, expected_cost)
        # Make sure output tour format starts and ends with depot city
        self.assertIn(self.tour[0], [0])
        self.assertIn(self.tour[-1], [0])

    def test_total_travel_cost_calculation(self):
        # Verify travel cost is the sum of distances in the tour, including return to depot
        expected = 0
        for i in range(len(self.tour)-1):
            expected += euclidean_data(self.cities[self.tour[i]], self.cities[self.tour[i+1]])
        self.assertEqual(expected, float('inf'))  # 'inf' indicates error or uncalculable situation in test

if __name__ == '__main__':
    unit_test_output = unittest.main(argv=[''], verbosity=2, exit=False)
    if unit_test_output.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")