import numpy as np

# City coordinates (index corresponds to city index)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Given tours and costs
tours = [
    [0, 16, 17, 15, 9, 11, 0],
    [1, 7, 13, 21, 20, 18, 1],
    [2, 5, 8, 4, 19, 2],
    [3, 6, 10, 12, 14, 3]
]

given_costs = [133.5566725340104, 200.71352933197454, 197.14533401544153, 111.18748613834666]

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tours(tours, coordinates, given_costs):
    # Validate if all cities are covered exactly once
    all_cities_visited = set()
    for tour in tours:
        all_cities_visited.update(tour[:-1])  # Ignore the last city because it's the return to depot
    
    if len(all_cities_visited) != len(coordinates):
        return "FAIL"

    # Calculate and compare costs
    accumulated_cost = 0
    for tour, given_cost in zip(tours, given_costs):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        
        # Compare calculated tour cost with given cost
        if not np.isclose(tour_cost, given_cost, atol=0.001):
            return "FAIL"
        
        accumulated_cost += tour_cost

    # Overall cost (not needed strictly as per given test case conditions but included for thoroughness)
    total_given_cost = sum(given_costs)
    if not np.isclose(accumulated_cost, total_given_cost, atol=0.001):
        return "FAIL"

    return "CORRECT"

# Test if everything is okay with the provided tours and costs
result = validate_tours(tours, coordinates, given_costs)
print(result)