import unittest
from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (29, 51),  # Depot city
            (49, 20),
            (79, 69),
            (17, 20),
            (18, 61),
            (40, 57),
            (57, 30),
            (36, 12),
            (93, 43),
            (17, 36),
            (4, 60),
            (78, 82),
            (83, 96),
            (60, 50),
            (98, 1)
        ]
        self.tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
        self.reported_total_cost = 442.57
        self.reported_max_distance = 85.21
    
    def test_tour_starts_and_ends_at_depot(self):
        start_city = self.tour[0]
        end_city = self.tour[-1]
        self.assertEqual(start_city, 0, "Tour does not start at depot city")
        self.assertEqual(end_city, 0, "Tour does not end at depot city")

    def test_visit_each_city_exactly_once(self):
        city_visits = set(self.tour[:-1])  # Exclude the last city since it's the return to depot
        expected_visits = set(range(15))  # All city indices
        self.assertEqual(city_visits, expected_visits, "Not all cities are visited exactly once")

    def test_objective_is_possible_approximation(self):
        distances = []
        for i in range(1, len(self.tour)):
            x1, y1 = self.cities[self.tour[i-1]]
            x2, y2 = self.cities[self.tour[i]]
            distances.append(calculate_euclidean_distance(x1, y1, x2, y2))
        
        max_distance = max(distances)
        total_distance = sum(distances)
        
        # As we cannot check for minimum max_distance due to lack of optimal value, we can only validate the reported distances
        self.assertAlmostEqual(max_distance, self.reported_max_distance, delta=max_distance * 0.01, msg="Reported maximum distance between cities is incorrect")
        self.assertAlmostEqual(total_distance, self.reported_total_cost, delta=total_distance * 0.01, msg="Reported total distance is incorrect")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTSPSolution)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")