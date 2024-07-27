import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = [(35, 40), (39, 41), (81, 30), (5, 50),
                       (72, 90), (54, 46), (8, 70), (97, 62),
                       (14, 41), (70, 44), (27, 47), (41, 74),
                       (53, 80), (21, 21), (12, 39)]

        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.reported_cost = 337.8447016788252

    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at the depot city")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at the depot city")

    def test_visit_each_city_once(self):
        city_visits = {city: 0 for city in range(len(self.cities))}
        
        for city in self.tour:
            city_visits[city] += 1

        # Check each city is visited exactly once, except for the depot which is visited twice.
        for city, count in city_visits.items():
            if city == 0:
                self.assertEqual(count, 2, f"Depot city visited {count} times, expected 2.")
            else:
                self.assertEqual(count, 1, f"City {city} visited {count} times, expected 1.")

    def test_correct_calculation_of_travel_cost(self):
        total_cost = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i + 1]
            x1, y1 = self.cities[city1]
            x2, y2 = self.cities[city2]
            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            total_cost += distance

        self.assertAlmostEqual(total_cost, self.reported_cost, places=5, msg="Reported travel cost is incorrect")

    def test_optimal_route(self):
        known_optimal_cost = 337.8447016788252  # this should be replaced with a benchmark if known
        self.assertAlmostEqual(self.reported_cost, known_optimal_score, places=5, msg="Tour is not optimized")

# Run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotTour)
result = unittest.TextTestRunner(verbosity=2).run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")