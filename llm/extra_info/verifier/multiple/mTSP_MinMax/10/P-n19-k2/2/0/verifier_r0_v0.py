import math
from itertools import chain

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_tsp_vrp_solution():
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), 
        (31, 62), (52, 33), (42, 41), (52, 41), 
        (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 27), (37, 69), (61, 33), 
        (62, 63), (63, 69), (45, 35)
    ]
    
    robot_tours = [
        [0, 6, 7, 5, 9, 16, 17, 10, 4, 14, 0],
        [0, 1, 2, 18, 13, 15, 8, 3, 12, 11, 0]
    ]
    
    expected_costs = [145.9, 146.62]
    expected_max_cost = 146.62
    
    # Concatenate the unique city indices from tours, except the depot (0).
    visited_cities = set(chain.from_iterable(tour[1:-1] for tour in robot_tours))
    
    # Test if each city is visited exactly once.
    exactly_once_visited = len(visited_cities) == 18
    
    # Calculate costs.
    calculated_costs = [calculate_travel_cost(tour, coordinates) for tour in robot_tours]
    calculated_max_cost = max(calculated_costs)
    
    # Floating point comparison tolerance.
    tolerance = 1e-2
    
    # Check if all costs are within a reasonable epsilon range.
    cost_comparison = all(abs(calculated_costs[i] - expected_costs[i]) < tolerance for i in range(2))
    max_cost_comparison = abs(calculated_max_cost - expected_max_cost) < tolerance
    
    if exactly_once_visited and cost_comparison and max_cost_comparison:
        print("CORRECT")
    else:
        print("FAIL")

test_tsp_vrp_solution()