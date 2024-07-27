import unittest
from math import sqrt

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Test class
class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (29, 51),  # Depot city 0
            (49, 20),  # City 1
            (79, 69),  # City 2
            (17, 20),  # City 3
            (18, 61),  # City 4
            (40, 57),  # City 5
            (57, 30),  # City 6
            (36, 12),  # City 7
            (93, 43),  # City 8
            (17, 36),  # City 9
            (4, 60),   # City 10
            (78, 82),  # City 11
            (83, 96),  # City 12
            (60, 50),  # City 13
            (98, 1)    # City 14
        ]
        self.grouped_cities = [
            [1, 2, 5, 6],
            [8, 9, 10, 13],
            [3, 4, 7],
            [11, 12, 14]
        ]
        self.solution_tour = [0, 5, 10, 4, 11, 0]
        self.reported_cost = 184.24

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "The tour should start at the depot city.")
        self.assertEqual(self.solution_tour[-1], 0, "The tour should end at the depot city.")

    def test_visit_one_city_from_each_group(self):
        selected_cities = self.solution_tour[1:-1]  # Excluding the starting and ending depot city
        for group in self.grouped_cities:
            self.assertEqual(len(set(group) & set(selected_cities)), 1, f"The tour should visit exactly one city from each group: {group}")

    def test_travel_cost(self):
        calculated_cost = 0
        for i in range(1, len(self.solution_tour)):
            city_a = self.solution_tour[i - 1]
            city_b = self.solution_tour[i]
            calculated_cost += euclidean_distance(self.cities[city_a], self.cities[city_b])
        calculated_cost = round(calculated0_cost, 2)
        self.assertAlmostEqual(calculated_cost, self.reported_cost, places=2, msg="The total travel cost should match the reported cost.")

# Run the test
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
    result = unittest.TextTestRunner().run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")