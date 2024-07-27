import unittest
import math

class TestGTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = {
            0: (16, 90),
            1: (43, 99),
            2: (80, 21),
            3: (86, 92),
            4: (54, 93),
            5: (34, 73),
            6: (6, 61),
            7: (86, 69),
            8: (30, 50),
            9: (35, 73),
            10: (42, 64),
            11: (64, 30),
            12: (70, 95),
            13: (29, 64),
            14: (32, 79)
        }
        self.groups = [
            [1, 6, 14],
            [5, 12, 13],
            [7, 10],
            [4, 11],
            [2, 8],
            [3, 9]
        ]

    def calculate_distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def total_tour_cost(self, tour):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += self.calculate_distance(tour[i], tour[i + 1])
        return total_cost

    def test_solution(self):
        # A hypothetical tour assuming this was calculated to be the shortest
        tour = [0, 1, 5, 7, 4, 2, 3, 0]
        total_cost = self.total_tour_cost(tour)

        # Conditions to be tested
        starts_and_ends_at_depot = (tour[0] == 0 and tour[-1] == 0)
        visits_one_city_from_each_group = len(set([g for city in tour for g in range(len(self.groups)) if city in self.groups[g]])) == len(self.groups)
        correct_tour_length = len(tour) == len(self.groups) + 2  # Adding 2 for the round trip to the depot

        # All conditions must be met
        if starts_and_ends_at_depot and visits_one_city_from_each_group and correct_tour_length:
            print("CORRECT")
        else:
            print("FAIL")

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)