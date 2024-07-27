import unittest
import math

class TestSolutionValidity(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (84, 67),
            1: (74, 40),
            2: (71, 13),
            3: (74, 82),
            4: (97, 28),
            5: (0, 31),
            6: (8, 62),
            7: (74, 56),
            8: (85, 71),
            9: (6, 76)
        }
        self.tour = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
        self.maximum_distance = 68.26

    def test_starts_and_ends_at_depot(self):
        self.assertEqual(self.tour[0], 0, "Tour does not start at depot city.")
        self.assertEqual(self.tour[-1], 0, "Tour does not end at depot city.")

    def test_visits_each_city_once(self):
        # Check if each city except the depot is visited exactly once, and depot is visited twice
        city_counts = {i: 0 for i in range(10)}
        for city in self.tour:
            city_counts[city] += 1
        for city in range(1, 10):
            self.assertEqual(city_counts[city], 1, f"City {city} is not visited exactly once.")
        self.assertEqual(city_counts[0], 2, "Depot city (0) is not visited exactly twice.")

    def test_maximum_distance_between_cities(self):
        # Calculate max distance to verify
        calculated_max_distance = 0
        for i in range(len(self.tour) - 1):
            x1, y1 = self.cities[self.tour[i]]
            x2, y2 = self.cities[self.tour[i+1]]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            calculated_max_distance = max(calculated_max_to_distance, distance)
        
        # Ensuring the provided maximum is accurate
        self.assertAlmostEqual(calculated_max_distance, self.maximum_distance, places=2, 
                               msg=f"Calculated max distance {calculated_max_distance} does not match the provided maximum distance {self.maximum_distance}")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)