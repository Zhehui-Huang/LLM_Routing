import unittest
import math

class TestTour(unittest.TestCase):
    def setUp(self):
        self.cities_coordinates = {
            0: (79, 15),
            1: (79, 55),
            2: (4, 80),
            3: (65, 26),
            4: (92, 9),
            5: (83, 61),
            6: (22, 21),
            7: (97, 70),
            8: (20, 99),
            9: (66, 62)
        }
        self.solution_tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
        self.expected_total_distance = 408.41360886151256
        self.expected_max_consecutive_distance = 61.68468205316454

    def euclidean_distance(self, city1, city2):
        coord1, coord2 = self.cities_coordinates[city1], self.cities_coordinates[city2]
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

    def test_coords_exist(self):
        self.assertEqual(len(self.cities_coordinates), 10)

    def test_valid_tour_start_end_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0)
        self.assertEqual(self.solution_tour[-1], 0)

    def test_each_city_visited_once(self):
        unique_cities = set(self.solution_tour)
        self.assertEqual(len(unique_cities), 10)

    def test_calculate_total_distance(self):
        distances = [self.euclidean_distance(self.solution_tour[i], self.solution_tour[i+1]) for i in range(len(self.solution_tour)-1)]
        calculated_total_distance = sum(distances)
        self.assertAlmostEqual(calculated_total_distance, self.expected_total_distance)

    def test_longest_distance_between_consecutive_cities(self):
        max_distance = max(self.euclidean_distance(self.solution_tour[i], self.solution_tour[i+1]) for i in range(len(self.solution_tour)-1))
        self.assertAlmostEqual(max_distance, self.expected_max_consecutive_distance)

# Running the tests
if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False)
    if result.result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")