import unittest
import math

def calculate_distance(city1, cityść2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # City coordinates
        self.cities = {
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
        # Groups of cities
        self.groups = [
            [5, 6, 7],
            [2, 3],
            [1, 9],
            [4, 8]
        ]
        # Provided tour solution
        self.tour = [0, 5, 2, 9, 8, 0]
        self.reported_cost = 183.99

    def test_tour_verification(self):
        errors = []

        # Check start and end at depot
        if not (self.tour[0] == 0 and self.tour[-1] == 0):
            errors.append("Tour does not start or end at the depot.")

        # Check visiting one city from each group
        visited_groups = set()
        for city in self.tour[1:-1]:
            for idx, group in enumerate(self.groups):
                if city in group:
                    visited_groups.add(idx)
        if len(visited_groups) != 4:
            errors.append("Tour does not visit exactly one city from each group.")

        # Check travel cost calculation
        total_distance = 0
        for i in range(len(self.tour) - 1):
            total_distance += calculate_distance(self.cities[self.tour[i]], self.cities[self.tour[i + 1]])
        if not math.isclose(total_distance, self.reported_cost, rel_tol=1e-2):
            errors.append("Reported total travel cost does not match the calculated cost.")

        if not errors:
            print("CORRECT")
        else:
            print("FAIL", errors)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)