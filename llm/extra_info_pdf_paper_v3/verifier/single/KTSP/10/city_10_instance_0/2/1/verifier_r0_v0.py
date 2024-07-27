import unittest
from math import sqrt

class TestTravelingRobot(unittest.TestCase):
    def setUp(self):
        # City coordinates with the index corresponding to the city number
        self.coordinates = {
            0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
            4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
            8: (61, 90), 9: (42, 49)
        }
        # Proposed solution details
        self.tour = [0, 9, 5, 6, 0]
        self.reported_cost = 61.66
    
    def test_cities_count(self):
        # There are exactly 10 cities including the depot city
        self.assertEqual(len(self.coordinates), 10)
    
    def test_start_end_depot(self):
        # Tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)
    
    def test_tour_length(self):
        # Robot visits exactly 4 cities
        self.assertEqual(len(set(self.tour)), 4 + 1)  # +1 because the starting and ending city is the same
    
    def calculate_euclidean_distance(self, city1, city2):
        x1, y1 = self.coordinates[city1]
        x2, y2 = self.coordinates[city2]
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def test_travel_cost(self):
        # Calculate total travel cost and compare with reported cost
        total_cost = sum(self.calculate_euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2)

    def test_tour_validity(self):
        # Check if each city in the tour is among the defined cities
        for city in self.tour:
            self.assertIn(city, self.coordinates)

    def runTest(self):
        test_methods = [
            self.test_cities_count, self.test_start_end_depot, self.test_tour_length,
            self.test_travel_cost, self.test_tour_validity
        ]
        for method in test_methods:
            method()
        print("CORRECT")

# Execute the unit tests
test_suite = unittest.TestSuite()
test_suite.addTest(TestTravelingRobot())
unittest.TextTestRunner().run(test_suite)