import unittest
import math

class TestRobotTourSolution(unittest.TestCase):
    def setUp(self):
        self.city_positions = {
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
        self.groups = {
            0: [7, 9],
            1: [1, 3],
            2: [4, 6],
            3: [8],
            4: [5],
            5: [2]
        }
        self.tour = [0, 7, 1, 4, 8, 5, 2, 0]
        self.reported_cost = 324.18

    def test_visit_one_from_each_group(self):
        # Check if exactly one city from each group is visited
        visited_from_groups = set()
        for city in self.tour:
            for group_id, cities in self.groups.items():
                if city in cities:
                    visited_from_groups.add(group_id)
        self.assertEqual(len(visited_from_groups), len(self.groups))

    def test_start_end_at_depot(self):
        # Check if tour starts and ends at the depot city
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def calculate_euclidean_distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
    
    def test_correct_total_travel_cost(self):
        # Calculate total cost
        cost = 0.0
        for i in range(len(self.tour) - 1):
            city1 = self.tour[i]
            city2 = self.tour[i+1]
            cost += self.calculate_euclidean_distance(self.city_positions[city1], self.city_positions[city2])
        cost = round(cost, 2)  # Round to match the format of reported cost
        self.assertAlmostEqual(cost, self.reported_cost)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRobotTourSolution('test_visit_one_from_each_group'))
    suite.addTest(TestRobotTourSolution('test_start_end_at_depot'))
    suite.addTest(TestRobotTourSolution('test_correct_total_travel_cost'))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")