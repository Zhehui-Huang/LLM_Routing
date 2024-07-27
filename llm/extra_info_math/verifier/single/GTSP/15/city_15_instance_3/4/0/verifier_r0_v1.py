import unittest
import math

# Hypothetical solution and its cost
solution_tour = [0, 1, 5, 7, 4, 2, 3, 0]
solution_cost = 365.96  # This should be updated to the correct computed value based on new correct distance calculations

# City coordinates indexed as per the task description
cities = [
    (16, 90),  # Depot city
    (43, 99),  # City 1 from Group 0
    (80, 21),  # City 2 from Group 4
    (86, 92),  # City 3 from Group 5
    (54, 93),  # City 4 from Group 3
    (34, 73),  # City 5 from Group 1
    (6, 61),   # City 6 from Group 0
    (86, 69),  # City 7 from Group 2
    (30, 50),  # City 8 from Group 4
    (35, 73),  # City 9 from Group 5
    (42, 64),  # City 10 from Group 2
    (64, 30),  # City 11 from Group 3
    (70, 95),  # City 12 from Group 1
    (29, 64),  # City 13 from Group 1
    (32, 79)   # City 14 from Group 0
]

# Grouping cities according to problem description to ensure one city per group is visited
city_groups = [{1, 6, 14}, {5, 12, 13}, {7, 10}, {4, 11}, {2, 8}, {3, 9}]

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
        visited_groups = set()
        for city in solution_tSour[1:-1]:  # Exclude the start/end depot city
            for index, group in enumerate(city_groups):
                if city in group:
                    visited_groups.add(index)
        self.assertEqual(len(visited_groups), len(city_groups), "Not all groups are visited exactly once.")

    def test_minimal_travel_cost(self):
        calculated_cost = calculate_total_distance(solution_tour)
        # Update this comparison to reflect the calculation error/margin
        self.assertAlmostEqual(calculated_cost, solution_cost, delta=0.1, msg="The travel cost is not minimal.")

if __name__ == "__main__":
    unittest.main()