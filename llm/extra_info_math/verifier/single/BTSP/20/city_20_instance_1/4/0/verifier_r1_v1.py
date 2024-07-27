def verify_solution(tour, total_cost, max_distance):
    # City coordinates dictionary
    coordinates = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
        6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
        18: (50, 28), 19: (69, 9)
    }
    
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if len(set(tour[1:-1])) != len(coordinates) - 1:  # Exclude depot repetitions
        return "FAIL"
    
    # Requirement 3: Minimize the maximum distance between consecutive cities
    def euclidean_distance(city1, city2):
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    consecutive_distances = [euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
    
    if abs(calculated_cost - total_cost) > 1e-5 or abs(max(consecutive_distances) - max_distance) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Data from the problematic output provided earlier
tour = [0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0, 17, 0]
total_travel_cost = 1255.3883861180173
maximum_distance = 62.76941930590086

# Run the verification
solution_status = verify_solution(tour, total_travel_cost, maximum_distance)
print(solution_status)