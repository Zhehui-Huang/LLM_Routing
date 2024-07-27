import unittest
from math import sqrt

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.coordinates = {
            0: (53, 68),
            1: (75, 11),
            2: (91, 95),
            3: (22, 80),
            4: (18, 63),
            5: (54, 91),
            6: (70, 14),
            7: (97, 44),
            8: (17, 69),
            9: (95, 89)
        }
        self.groups = {
            0: [5, 6, 7],
            1: [2, 3],
            2: [1, 9],
            3: [4, 8]
        }
        self.depot = 0
        self.tour = [0, 9, 5, 3, 8, 0]
        self.reported_cost = 169.94

    def test_cities_count(self):
        self.assertEqual(len(self.coordinates), 10, "The number of cities does not match 10.")

    def test_groups_count(self):
        self.assertEqual(len(self.groups), 4, "The number of groups does not match 4.")

    def test_start_end_depot(self):
        self.assertEqual(self.tour[0], self.depot, "Tour does not start at the depot.")
        self.assertEqual(self.tour[-1], self.depot, "Tour does not end at the depot.")
        
    def test_visit_one_from_each_group(self):
        visited = set(self.tour[1:-1])  # exclude depot start and end
        for group, cities in self.groups.items():
            self.assertEqual(len(visited.intersection(cities)), 1, "Not exactly one city from group {} was visited.".format(group))
        
    def test_calculate_total_cost(self):
        def euclidean_distance(city1, city2):
            x1, y1 = self.coordinates[city1]
            x2, y2 = self.coordinates[city2]
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        travel_cost = sum(euclidean_distance(self.tour[i], self.tour[i + 1]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(travel_cost, self.reported_cost, places=2, msg="Calculated cost does not match reported cost.")

def main():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(TestRobotTour))
    
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("CORRECT")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()