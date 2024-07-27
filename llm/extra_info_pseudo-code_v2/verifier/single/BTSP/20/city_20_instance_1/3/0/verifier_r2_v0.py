import unittest
import math

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
            (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
            (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
            (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
        ]
        self.tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
        self.total_travel_cost = 477.05
        self.max_distance = 87.46

    def test_unique_cities_once(self):
        # All cities visited only once except the depot which should be visited twice
        unique_cities = set(range(20))
        tour_cities = set(self.tour)
        self.assertEqual(tour_cities, unique_cities, "Not all cities were visited exactly once.")

    def test_tour_starts_ends_depot(self):
        # Tour should start and end at the depot (city 0)
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

    def test_calculate_total_travel_cost(self):
        # Calculate total travel cost
        calc_cost = 0
        for i in range(len(self.tour)-1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            calc_cost += distance
        self.assertAlmostEqual(calc_cost, self.total_travel_cost, places=2, msg="Total travel cost not matching.")

    def test_max_distance_between_consecutive_cities(self):
        # Calculate the maximum distance between consecutive cities
        max_dist = 0
        for i in range(len(self.tour)-1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if distance > max_dist:
                max_dist = distance
        self.assertAlmostEqual(max_dist, self.max_distance, places=2, msg="Maximum distance between consecutive cities not matching.")

if __name__ == '__main__':
    result = unittest.main(argv=[''], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")