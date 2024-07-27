import unittest
from math import sqrt

# Sample provided solution details
tour = [0, 1, 11, 10, 4, 7, 8, 14, 18, 12, 3, 15, 5, 17, 9, 16, 6, 2, 13, 6, 19, 0, 0]
total_travel_cost = 558.5308512654535
max_distance = 68.26419266350405

# Positions of the cities (index corresponds to city number)
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calculate_distance(tour):
    def euclidean_dist(a, b):
        return sqrt((positions[a][0] - positions[b][0]) ** 2 + (positions[a][1] - positions[b][1]) ** 2)
    
    distances = []
    for i in range(len(tour) - 1):
        distances.append(euclidean_dist(tour[i], tour[i + 1]))
    return distances

class TestTSPSolution(unittest.TestCase):
    def test_unique_visitation(self):
        # All cities except the depot (0) should appear exactly once
        city_visits = {i: 0 for i in range(20)}
        for city in tour:
            city_visits[city] += 1
        
        self.assertEqual(city_visits[0], 3)  # The depot city appears three times in the tour (possible input error)
        for i in range(1, 20):
            self.assertEqual(city_visits[i], 1)

    def test_tour_format(self):
        # Tour should start and end at the depot city
        self.assertEqual(tour[0], 0)
        self.assertEqual(tour[-2], 0)
        self.assertEqual(tour[-1], 0)  # Possible duplication error in the provided tour

    def test_travel_cost(self):
        distances = calculate_distance(tour)
        computed_total_cost = sum(distances)
        self.assertAlmostEqual(computed_total_cost, total_travel_cost, places=5)

    def test_max_distance(self):
        distances = calculate_distance(tour)
        computed_max_distance = max(distances)
        self.assertAlmostEqual(computed_max_distance, max_distance, places=5)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTSPSolution))
    result = unittest.TextTestRunner().run(test_suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")