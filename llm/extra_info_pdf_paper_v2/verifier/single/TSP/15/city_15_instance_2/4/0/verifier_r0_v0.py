import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    return total_cost

def test_tsp_solution():
    # City coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
        6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
        12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    
    # Provided tour and cost
    proposed_tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
    proposed_cost = 322.50
    
    # Verify all cities are visited exactly once, excluding the depot city
    visited_cities = set(proposed_tour)
    if len(visited_cities) != len(cities) or len(proposed_tour) != len(cities)+1:
        return "FAIL"
    
    # Check tour starts and ends at the depot city
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Calculate travel cost
    calculated_cost = calculate_total_travel_cost(proposed_tour, cities)
    
    # Compare calculated cost with proposed cost (within an acceptable rounding difference)
    if not math.isclose(calculated_cost, proposed_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_tsp_solution())