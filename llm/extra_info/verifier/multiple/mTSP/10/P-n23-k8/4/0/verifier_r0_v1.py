import math

# Robot tours from the solution
robots_tours = [
    [0, 2, 8, 9, 13, 0],
    [0, 3, 12, 15, 0],
    [0, 6, 21, 0],
    [0, 14, 17, 0],
    [0, 1, 10, 16, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 5, 7, 20, 22, 0]
]

# Individual robot tour costs
individual_costs = [86.16, 78.2, 24.48, 69.36, 42.67, 89.42, 57.39, 77.66]

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tours, costs, total_expected_cost):
    # Check if all robots start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check all cities are visited once
    all_cities_visited = set(range(1, 23))  # Cities from 1 to 22 (exclude depot)
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour[1:-1])
    if visited_cities != all_cities_visited:
        return "FAIL"
    
    # Check if the travel costs are calculated correctly
    computed_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        computed_costs.append(round(tour_cost, 2))
    
    if computed_costs != costs:
        return "FAIL"

    # Check if the total cost is correct
    total_cost = sum(computed_costs)
    if round(total_cost, 2) != round(total_expected_cost, 2):
        return "FAIL"
    
    return "CORRECT"

# Checking the solution
result = verify_solution(robots_tours, individual_costs, 525.34)
print(result)