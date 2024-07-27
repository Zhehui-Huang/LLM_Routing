import unittest
import math

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (50, 42),
            1: (41, 1),
            2: (18, 46),
            3: (40, 98),
            4: (51, 69),
            5: (47, 39),
            6: (62, 26),
            7: (79, 31),
            8: (61, 90),
            9: (42, 49)
        }
        self.groups = {
            0: [1, 2, 6],
            1: [3, 7, 8],
            2: [4, 5, 9]
        }
        self.solution_tour = [0, 5, 6, 7, 0]
        self.reported_cost = 72.83

    def test_cities_count(self):
        self.assertEqual(len(self.cities), 10, "The number of cities should be 10.")

    def test_groups_validation(self):
        self.assertTrue(all(city in self.cities for group in self.groups.values() for city in group),
                        "All cities in groups should be in the cities list.")

    def test_robot_starts_and_ends_at_depot(self):
        self.assertEqual(self.solution_tour[0], 0, "Tour should start at depot city 0.")
        self.assertEqual(self.solution_tour[-1], 0, "Tour should end at depot city 0.")

    def test_one_city_per_group(self):
        visited_groups = set()
        for city in self.solution_tour[1:-1]:  # exclude the depot city in the calculation
            for group_id, members in self.groups.items():
                if city in members:
                    visited_groups.add(group_id)
        self.assertEqual(len(visited_groups), 3, "The tour must visit one city from each group.")

    def test_total_travel_cost(self):
        def euclidean_distance(city1, city2):
            return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

        total_cost = 0
        for i in range(len(self.solution_tour) - 1):
            city1_id, city2_id = self.solution_tour[i], self.solution_tour[i+1]
            city1_coords, city2_coords = self.cities[city1_id], self.cities[city2_id]
            total_cost += euclidean_distance(city1_coords, city2_coords)
        
        self.assertAlmostEqual(total_cost, self.reported_cost, places=2, 
                               msg=f"Reported travel cost should be approximately {self.reported_cost}")

    def test_solution(self):
        try:
            self.test_cities_count()
            self.test_groups_validation()
            self.test_robot_starts_and_ends_at_depot()
            self.test_one_city_per_group()
            self.test_total_travel_cost()
            return "CORRECT"
        except AssertionError as e:
            return f"FAIL: {str(e)}"

# Run the tests
if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestRobotTour('test_solution'))
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")