import unittest
from math import sqrt

# Provided coordinates
coordinates = [
    (14, 77),  # Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Provided solution tour and cost
provided_tour = [0, 3, 4, 10, 11, 16, 7, 5, 14, 6, 9, 2, 12, 13, 1, 8, 15, 18, 17, 19, 0]
provided_cost = 481.55

def calculate_euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return round(total_cost, 2)

class TestRobotTour(unittest.TestCase):
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(provided_tour[0], 0)
        self.assertEqual(provided_tour[-1], 0)

    def test_each_city_visited_once(self):
        # Check each city except the depot is in the tour exactly once
        cities = set(range(1, 20))
        tour_cities = set(provided_tour[1:-1])
        self.assertEqual(cities, tour_cities)

    def test_output_format(self):
        # Check if the output format is correct
        self.assertIsInstance(provided_tour, list)
        self.assertIsInstance(provided_cost, (float, int))

    def test_correct_total_travel_cost(self):
        calculated_cost = calculate_total_tour_cost(provided_tour, coordinates)
        self.assertAlmostEqual(calculated_cost, provided_cost)

# Run the tests
if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")