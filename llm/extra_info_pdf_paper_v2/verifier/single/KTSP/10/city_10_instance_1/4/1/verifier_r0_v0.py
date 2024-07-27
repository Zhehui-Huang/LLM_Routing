import unittest
import math

# Define the cities' coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Provided solution
tour = [0, 4, 8, 3, 5, 0]
total_travel_cost = 110.38072506104011

def calculate_total_distance(tour):
    def distance(city1, city2):
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

class TestTourSolution(unittest.TestCase):
    def test_city_count(self):
        self.assertEqual(len(cities), 10)

    def test_tour_start_end_depot(self):
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-1], 0)

    def test_tour_length_including_depot(self):
        self.assertEqual(len(tour), 6)  # depots are included at both start and end

    def test_tour_distance_calculation(self):
        computed_cost = calculate_total_distance(tour)
        self.assertAlmostEqual(computed_cost, total_travel_cost, places=5)

    def test_tour_uniqueness(self):
        unique_cities = set(tour)
        self.assertTrue(len(unique_cities) <= 5)  # <= 5 unique cities, including the depot twice

    def test_tour_representation_correctness(self):
        self.assertIsInstance(tour, list)
        self.assertIsInstance(total_travel_report, float)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
result = unittest.TextTestRunner().run(suite)

if result.wasSuccessful():
    print("CORRECT")
else:
    print("FAIL")