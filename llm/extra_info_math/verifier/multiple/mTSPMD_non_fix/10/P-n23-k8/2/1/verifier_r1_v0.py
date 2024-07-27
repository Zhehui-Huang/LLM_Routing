import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def check_solution(tours, city_coords):
    # Requirement: each city is visited exactly once
    all_visited = set()
    for tour in tours:
        for city in tour:
            if city in all_visited and city != 0:  # Except the depot can appear multiple times
                return "FAIL"
            all_visited.add(city)
            
    # Check if all cities visited
    if len(all_visited) != len(city_coords):
        return "FAIL"
    
    # Ensure exactly one robot leaves the depot initially
    if not all(tour[0] == 0 for tour in tours):
        return "FAIL"
    
    # Ensure minimum travel cost
    # Calculating total travel cost by the solver output
    solver_total_cost = 235.67331696088496
    calculated_total_cost = 0
    
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        calculated_total_cost += tour_cost
    
    # Comparing calculated and given costs
    if not math.isclose(solver_total_cost, calculated_total_tost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours
tours = [
    [0, 1, 0, 2, 0, 6, 0, 7, 0, 10, 0, 16, 0, 20, 0, 21, 0],  # Only robot 0 operating
    [0], [0], [0], [0], [0], [0], [0]  # All other robots staying at depot
]

# Check solution correctness
result = check_solution(tours, city_coords)
print(result)