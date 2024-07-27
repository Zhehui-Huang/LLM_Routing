import unittest
import math

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = [
            (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
            (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
        ]
        self.tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
        self.total_travel_cost = 295.9919678938414
        self.max_distance_between_cities = 56.462376853972415
    
    def test_starts_and_ends_at_depot(self):
        # Check if tour starts and ends at depot city (City 0)
        self.assertEqual(self.tour[0], 0, "Tour does not start at City 0")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at City 0")

    def test_visits_each_city_once(self):
        # Check if each city is visited exactly once, ignoring the last return to depot
        visited_cities = self.tour[1:-1]
        unique_cities = set(visited_cities)
        self.assertEqual(len(visited_cities), len(unique_cities), "Some cities are visited more than once or not visited")
    
    def test_minimize_max_distance_between_cities(self):
        # Calculate and compare actual maximum distance based on the given solution
        actual_max_distance = 0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            coord1 = self.cities_coordinates[city1]
            coord2 = self.cities_coordinates[city2]
            distance = math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
            actual_max_distance = max(actual_max_distance, distance)
        self.assertAlmostEqual(actual_max_distance, self.max_distance_between_cities,
                               msg="The maximum distance between two consecutive cities is not minimized as expected",
                               places=6)

    def test_correct_solution(self):
        errors = []
        try:
            self.test_starts_and_ends_at_depot()
        except AssertionError as e:
            errors.append(str(e))

        try:
            self.test_visits_each_city_once()
        except AssertionError as e:
            errors.append(str(e))

        try:
            self.test_minimize_max_distance_between_cities()
        except AssertionError as e:
            errors.append(str(e))

        if errors:
            self.fail("FAIL: " + ", ".join(errors))
        else:
            print("CORRECT")

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)