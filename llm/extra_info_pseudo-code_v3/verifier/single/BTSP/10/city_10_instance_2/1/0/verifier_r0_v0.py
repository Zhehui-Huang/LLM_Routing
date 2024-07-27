import unittest
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_tour(tour, distances):
    # Check if tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Check if every city is visited exactly once
    visited = set(tour)
    if len(visited) != len(tour) - 1 or visited != set(range(len(tour) - 1)):
        return False

    # Check total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = distances[(tour[i], tour[i+1])]
        total_cost += d
        if d > max_distance:
            max_distance = d

    # Assuming some function returning calculated outputs and the distances dictionary
    output_tour, output_total_cost, output_max_distance = get_algorithm_output(distances)

    return (output_tour == tour and
            abs(output_total_cost - total_cost) < 1e-6 and
            abs(output_max_distance - max_distance) < 1e-6)

# Simulate get_algorithm_output function based on predefined inputs
def get_algorithm_output(distances):
    # Just a mocked example for testing purposes
    return [0, 1, 2, 3, 0], 100, 40

class TestSolution(unittest.TestCase):
    def test_solution(self):
        # Cities layout
        cities = {
            0: (90, 3),
            1: (11, 17),
            2: (7, 27),
            3: (95, 81),
            4: (41, 54),
            5: (31, 35),
            6: (23, 95),
            7: (20, 56),
            8: (49, 29),
            9: (13, 17)
        }
        
        # Calculate distances between all pairs of cities
        distances = {}
        for i in cities:
            for j in cities:
                if i != j:
                    distances[(i, j)] = calculate_distance(cities[i], cities[j])
        
        # Example tour (you would be replacing this from your algorithm's output)
        tour = [0, 1, 2, 3, 0]  # This is a dummy tour for example purposes
        
        # Check tour validity
        result = check_tour(tour, distances)
        
        # Depending on whether all checks passed
        self.assertTrue(result)

# Run tests
unittest.main(argv=[''], verbosity=2, exit=False)