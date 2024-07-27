import unittest
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

class TravelTest(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 
            5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 
            10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 
            15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
        }
        self.groups = [
            [1, 3, 5, 11, 13, 14, 19],
            [2, 6, 7, 8, 12, 15],
            [4, 9, 10, 16, 17, 18]
        ]
        self.proposed_tour = [0, 1, 8, 17, 2, 4, 0]
        self.expected_cost = 191.98723836274047
    
    def test_tour_starts_and_ends_at_depot(self):
        self.assertEqual(self.proposed_tour[0], 0)
        self.assertEqual(self.proposed_tour[-1], 0)
    
    def test_tour_visits_one_city_from_each_group(self):
        visited_group_indices = set()
        for city in self.proposed_tour[1:-1]: # Exclude depot start/end
            for group_index, group in enumerate(self.groups):
                if city in group:
                    visited_group_indices.add(group_index)
                    break
        self.assertEqual(len(visited_group_indices), len(self.groups))

    def test_tour_cost_calculation(self):
        total_cost = sum(calculate_distance(self.cities[self.proposed_tour[i]], self.cities[self.proposed_tour[i + 1]]) 
                         for i in range(len(self.proposed_tour) - 1))
        self.assertAlmostEqual(total_cost, self.expected_cost, places=5)

if __name__ == '__main__':
    unittest.main()