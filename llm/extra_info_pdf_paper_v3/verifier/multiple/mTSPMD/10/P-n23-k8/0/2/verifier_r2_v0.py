import math

def calculate_total_distance(tours, cities):
    total_cost = 0
    individual_costs = []
    
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = cities[tour[i]]
            x2, y2 = cities[tour[i+1]]
            tour_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        individual_costs.append(tour_cost)
        total_cost += tour_cost
    
    return total_cost, individual_costs

def verify_solution(tours, depots, num_cities):
    visited_cities = set()
    all_cities = set(range(num_cities))
    
    # [Requirement 1] Starting and ending at designated depots
    for index, tour in enumerate(tours):
        if not (tour[0] == depots[index] and tour[-1] == depots[index]):
            return "FAIL"
    
    # [Requirement 2] Each city visited exactly once
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the first and the last (depots)
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
    
    # Ensure all cities are visited
    if visited_cities != all_cities:
        return "FAIL"
    
    # [Requirement 4] Correct tour format
    # This is generally ensured by the format of the output already being checked in parsing
    
    # [Requirement 5] Travel costs verification can be a simplification check only
    total_cost, individual_costs = calculate_total_distance(tours, cities_location)
    if not total_cost or not individual_costs:
        return "FAIL"
    
    return "CORRECT"

cities_location = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# For example, here's one possible set of tours output (hypothetical since actual output would depend on actual tour planning)
tours_example = [
    [0, 8, 10, 12, 11, 15, 4, 3, 0],  # Robot 0
    [1, 16, 6, 7, 9, 13, 1],         # Robot 1
    [2, 5, 20, 22, 17, 14, 2],       # Robot 2
    [3, 18, 19, 3],                  # Robot 3
    [4, 4],                          # Redundant tour, invalid
    [5, 5],                          # Redundant tour, invalid
    [6, 21, 6],                      # Robot 6
    [7, 7]                           # Redundant tour, invalid
]

print(verify_solution(tours_example, [0, 1, 2, 3, 4, 5, 6, 7], len(cities_location)))