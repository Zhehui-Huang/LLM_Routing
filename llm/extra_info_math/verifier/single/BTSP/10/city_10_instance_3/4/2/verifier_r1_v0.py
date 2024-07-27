def verify_tsp_solution(tour, total_travel_cost, max_consecutive_distance):
    # Define city coordinates
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Requirement 1: Start and end at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Requirement 3: Minimize the maximum distance between any consecutive cities
    import math
    calculated_max_distance = 0
    calculated_total_cost = 0
    
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    if abs(total_travel_cost - calculated_total_cost) > 0.0001:
        return "FAIL"
    if abs(max_consecutive_distance - calculated_max_distance) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Test the solution
solution_status = verify_tsp_solution(
    tour=[0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0],
    total_travel_cost=913.8927727036689,
    max_consecutive_distance=91.3892772703669
)

print(solution_status)