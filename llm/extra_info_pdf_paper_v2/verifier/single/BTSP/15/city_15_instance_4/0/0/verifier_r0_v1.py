import unittest
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestBTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [
            (35, 40),  # Depot: City 0
            (39, 41),  # City 1
            (81, 30),  # City 2
            (5, 50),   # City 3
            (72, 90),  # City 4
            (54, 46),  # City 5
            (8, 70),   # City 6
            (97, 62),  # City 7
            (14, 41),  # City 8
            (70, 44),  # City 9
            (27, 47),  # City 10
            (41, 74),  # City 11
            (53, 80),  # City 12
            (21, 21),  # City 13
            (12, 39)   # City 14
        ]
        self.tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
        self.total_cost = 337.8447016788252
        self.max_distance = 60.67124524847005

    def test_requirement_1(self):
        # Test if tour starts and ends at depot city 0
        self.assertEqual(self.tour[0], 0)
        self.assertEqual(self.tour[-1], 0)

    def test_requirement_2(self):
        # Test if each city is visited exactly once, except the depot city visited twice
        unique_visits = set(self.tour)
        all_cities = set(range(15))  # Cities 0 to 14
        self.assertEqual(unique_visits, all_cities)

    def test_requirement_3(self):
        # Test if tour cost is calculated as the Euclidean distance
        calculated_cost = sum(euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1))
        self.assertAlmostEqual(calculated_cost, self.total_cost, places=5)

    def test_requirement_4_and_7(self):
        # Test if max distance objectives are met
        distances = [euclidean_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]]) for i in range(len(self.tour) - 1)]
        max_dist = max(distances)
        self.assertAlmostEqual(max_dist, self.max_distance, places=5)

    def test_total_requirements(self):
        try:
            self.test_requirement_1()
            self.test_requirement_2()
            self.test_requirement_3()
            self.test_requirement_4_and_7()
        except AssertionError:
            self.fail("Some requirements were not met. FAIL")
        else:
              print("All requirements met. CORRECT")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)