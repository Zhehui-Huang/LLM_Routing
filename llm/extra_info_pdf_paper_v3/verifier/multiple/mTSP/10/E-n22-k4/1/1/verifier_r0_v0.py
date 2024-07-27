import math

# All the input data for cities and their coordinates.
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

tours = [
    [0, 14, 16, 12, 13, 10, 0],
    [0, 15, 17, 11, 8, 9, 0],
    [0, 18, 19, 6, 7, 20, 0],
    [0, 21, 5, 4, 3, 2, 1, 0]
]

# Expected results for each tour and overall total cost from the solution.
expected_costs = [101.65864442938738, 150.40166870539406, 228.23967386853874, 228.75688636631048]
expected_overall_cost = 709.0568733696307

def calculate_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tours, cities, expected_costs, expected_overall_cost):
    all_visited = set()
    computed_costs = []
    total_computed_cost = 0

    for tour in tours:
        tour_cost = 0
        visited_in_this_tour = set(tour)
        previous_city = tour[0]
        
        # Is the tour starting and ending at the depot?
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate cost of the current tour
        for city in tour[1:]:
            tour_cost += calculate_distance(cities[previous_city], cities[city])
            previous_city = city

        computed_costs.append(tour_cost)
        all_visited.update(visited_in_this_tour)
        total_computed_cost += tour_cost
    
    # Check if all city indices from 1 to 21 are uniquely visited and costs are accurate
    if len(all_visited) != 22 or all_visited != set(range(22)):
        return "FAIL"

    # Compare computed costs to expected costs with tolerance
    if not all(math.isclose(computed_costs[i], expected_costs[i], rel_tol=1e-9) for i in range(len(computed_costs))):
        return "FAIL"
    
    if not math.isclose(total_computed_cost, expected_overall_memory_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Verify the solution
result = verify_solution(tours, cities, expected_costs, expected_overilinxall_cost)
print(result)