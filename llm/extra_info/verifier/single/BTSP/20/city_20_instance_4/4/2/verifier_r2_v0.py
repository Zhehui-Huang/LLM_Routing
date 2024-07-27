import unittest
from math import sqrt

class TestSolutionValidation(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.coordinates = [
            (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
            (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
            (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
            (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
        ]
        self.tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
        self.reported_total_cost = 410.03585920085146
        self.reported_max_distance = 89.00561780022652

    def test_tour_start_end_at_depot(self):
        # Check if tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_visit_each_city_once(self):
        # Check if each city except depot is visited exactly once
        city_visits = {i: 0 for i in range(20)}
        for city in self.tour:
            city_visits[city] += 1
        self.assertTrue(all(count == 1 for i, count in city_visits.items() if i != 0))
        self.assertEqual(city_visits[0], 2)  # Start and end at Depot

    def test_total_travel_cost(self):
        # Compute the total travel cost
        total_cost = sum(
            sqrt((self.coordinates[self.tour[i]][0] - self.coordinates[self.tour[i+1]][0])**2 +
                 (self.coordinates[self.tour[i]][1] - self.coordinates[self.tour[i+1]][1])**2)
            for i in range(len(self.tour)-1)
        )
        self.assertAlmostEqual(total_cost, self.reported_total_cost, places=5)

    def test_max_consecutive_distance(self):
        # Compute the maximum distance between consecutive cities
        max_distance = max(
            sqrt((self.coordinates[self.tour[i]][0] - self.coordinates[self.tour[i+1]][0])**2 +
                 (self.coordinates[self.tour[i]][1] - self.coordinates[self.tour[i+1]][1])**2)
            for i in range(len(self.tour)-1)
        )
        self.assertAlmostEqual(max_distance, self.reported_max_distance, places=5)

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSolutionValidation))
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")