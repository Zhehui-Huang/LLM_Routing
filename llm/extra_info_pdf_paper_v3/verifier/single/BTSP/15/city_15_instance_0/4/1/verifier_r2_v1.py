import unittest
import math

# Define the city coordinates
cities = [
    (9, 93),  # City 0 - Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Solution tour and calculated costs
solution_tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
solution_total_cost = 373.97
solution_max_distance = 63.6

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tour(tour, cities):
    # Check if all cities are visited exactly once and tour starts/ends at depot
    all_cities_visited = set(tour) == set(range(len(cities)))
    starts_ends_at_depot = tour[0] == tour[-1] == 0

    # Calculate total cost and max distance
    distances = [calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)]
    total_cost = sum(distances)
    max_distance = max(distances)

    return starts_ends_at_depot, all_cities_visited, total_cost, max_distance

class TestTravelingSalesmanSolution(unittest.TestCase):
    def test_solution(self):
        starts_ends_at_depot, all_cities_visited, total_cost, max_distance = validate_tour(solution_tour, cities)
        
        self.assertTrue(starts_ends_at_depot, "The tour should start and end at the depot (city 0).")
        self.assertTrue(all_cities_visited, "The tour must visit each city exactly once.")
        self.assertAlmostEqual(total_cost, solution_total_cost, places=2, msg="Total travel cost should match the expected value.")
        self.assertAlmostEqual(max_distance, solution_max_distance, places=1, msg="Maximum distance between consecutive cities should match the expected value.")

# Run the test
if __name__ == '__main__':
    unittest.main()