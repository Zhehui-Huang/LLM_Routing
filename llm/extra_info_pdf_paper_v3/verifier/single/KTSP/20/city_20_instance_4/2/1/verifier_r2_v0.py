import unittest
import math

class TestTourValidation(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
            5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
            10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
            15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
        }
        self.total_cities = len(self.coordinates)
        self.depot_city = 0
        self.required_cities_count = 16
        self.submitted_tour = [7, 11, 18, 1, 14, 16, 2, 8, 15, 10, 0, 3, 6, 4, 9, 12, 0]
        self.submitted_cost = 653.6933138129884

    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def calculate_total_distance(self, tour):
        return sum(self.calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    def test_tour_length(self):
        # Expect 16 unique cities plus the closing back to depot city: length should be 17
        self.assertEqual(len(self.submitted_tour), self.required_cities_count + 1)  

    def test_tour_cities_count(self):
        # Tour should contain exactly 16 unique cities including the depot city
        self.assertEqual(len(set(self.submitted_tour)), self.required_cities_count)

    def test_tour_start_end_depot(self):
        # Start and end should be the depot city
        self.assertEqual(self.submitted_tour[0], self.depot_city)
        self.assertEqual(self.submitted_tour[-1], self.depot_city)

    def test_travel_cost(self):
        # Calculated cost should match the submitted cost
        calculated_cost = self.calculate_total_distance(self.submitted_tour)
        # Using approximation due to possible floating point arithmetic issues
        self.assertAlmostEqual(calculated_cost, self.submitted_cost, places=5)

    def test_valid_cities_in_tour(self):
        # All cities in the tour should be valid existing cities
        all_cities_valid = all(city in self.coordinates for city in self.submitted_tour)
        self.assertTrue(all_cities_valid)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTourValidation))
    test_runner = unittest.TextTestRunner()
    results = test_runner.run(test_suite)
    
    if results.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")