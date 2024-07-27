import unittest
import math

# Define cities and groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

groups = {
    0: [5, 6, 16], 1: [8, 18, 19], 2: [11, 12, 13], 3: [1, 3, 9], 
    4: [2, 4, 14], 5: [10, 17], 6: [7, 15]
}

# Provided tour and cost
provided_tour = [0, 8, 17, 13, 9, 6, 4, 15, 0]
provided_cost = 208.3243929659895

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_tour(tour, groups):
    """Check if the tour visits exactly one city from each group and starts/ends at the depot city."""
    visited_groups = []
    for i in range(1, len(tour) - 1):
        city = tour[i]
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return False
                visited_groups.append(group_id)
                break
    return len(visited_groups) == len(groups) and tour[0] == tour[-1] == 0

def validate_cost(tour, expected_cost):
    """Check if the total travel cost of the tour is calculated correctly."""
    total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return abs(total_cost - expected_cost) < 1e-5  # use a small delta to account for floating point precision


class TestProvidedSolution(unittest.TestCase):
    def test_validate_tour(self):
        self.assertTrue(validate_tour(provided_tour, groups), "The tour should visit exactly one city from each group and start/end at the depot.")

    def test_validate_cost(self):
        self.assertTrue(validate_cost(provided_tour, provided_cost), "The total cost of the provided tour should match the calculated cost.")

    def test_solution(self):
        valid_tour = validate_tour(provided_tour, groups)
        valid_cost = validate_cost(provided_tour, provided_cost)
        if valid_tour and valid_cost:
            print("CORRECT")
        else:
            print("FAIL")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)