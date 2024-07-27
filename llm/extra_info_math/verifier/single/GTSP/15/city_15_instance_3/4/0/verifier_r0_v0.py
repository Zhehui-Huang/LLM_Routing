import unittest
import math

# Hypothetical optimal tour solution and its cost that have been previously determined
solution_tour = [0, 1, 5, 7, 4, 2, 3, 0]
solution_cost = 385

# City coordinates indexed as per the task description
cities = [
    (16, 90),  # Depot city
    (43, 99),  # Group 0
    (80, 21),  # Group 4
    (86, 92),  # Group 5
    (54, 93),  # Group 3
    (34, 73),  # Group 1
    (6, 61),
    (86, 69),  # Group 2
    (30, 50),  # Group 4
    (35, 73),  # Group 5
    (42, 64),  # Group 2
    (64, 30),  # Group 3
    (70, 95),  # Group 1
    (29, 64),  # Group 1
    (32, 79)   # Group 0
]

# City groups as defined in the problem statement
city_groups = [
    {1, 6, 14},
    {5, 12, 13},
    {7, 10},
    {4, 11},
    {2, 8},
    {3, 9}
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_starts_and_ends_at_depot(self):
        self.assertEqual(solution_tour[0], 0, "The tour does not start at the depot.")
        self.assertEqual(solution_tour[-1], 0, "The tour does not end at the depot.")

    def test_visits_one_city_from_each_group(self):
        visited = {group: False for group in range(len(city_groups))}
        for city in solution_tour[1:-1]:  # Exclude the depot at beginning and end
            for group_index, group in enumerate(city_groups):
                if city in group:
                    visited[group_index] = True
                    continue
        self.assertTrue(all(visited.values()), "Not all groups are visited exactly once.")

    def test_minimal_travel_cost(self):
        calculated_cost = calculate_total_distance(solution_tour)
        self.assertAlmostEqual(calculated_cost, solution_cost, msg="The travel cost is not minimal.")

# Running the tests
if __name__ == "__main__":
    unittest.main()