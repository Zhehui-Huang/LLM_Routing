import unittest
from math import sqrt

def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class TestTourSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
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
        self.groups = [
            [1, 4],
            [2, 6],
            [7],
            [5],
            [9],
            [8],
            [3]
        ]
        self.robot_tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
        self.total_travel_cost = 371.1934423276749

    def test_number_of_cities(self):
        self.assertEqual(len(self.cities), 10)

    def test_depot_location(self):
        self.assertEqual(self.cities[0], (79, 15))

    def test_groups_coverage(self):
        visited_groups = {group_index: False for group_index in range(len(self.groups))}
        visited_cities = set()

        for city in self.robot_tour:
            if city == 0:
                continue
            for index, group in enumerate(self.groups):
                if city in group:
                    visited_groups[index] = True
                    visited_cities.add(city)
        
        self.assertTrue(all(visited_groups.values()))
        self.assertEqual(len(visited_cities), 7, "Each group needs a distinct city visited")

    def test_robot_returns_to_depot(self):
        self.assertEqual(self.robot_tour[0], 0)
        self.assertEqual(self.robot_tour[-1], 0)

    def test_travel_cost_calculation(self):
        calculated_cost = 0
        prev_city = self.robot_tour[0]
        
        for current_city in self.robot_tour[1:]:
            calculated_cost += calculate_euclidean_distance(
                self.cities[prev_city][0], self.cities[prev_city][1],
                self.cities[current_city][0], self.cities[current_city][1]
            )
            prev -- current_city
        
        self.assertAlmostEqual(calculated_cost, self.total_travel_cost)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTourSolution)
    result = unittest.TextTestRunner().run(suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")