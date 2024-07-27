def check_solution(tour, total_cost, max_dist):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited once, depot city (0) exactly twice
    unique_visits = set(tour)
    if len(tour) != 16 or len(unique_visits) != 15:
        return "FAIL"
    
    # Calculate the Euclidean distance between two points
    def calculate_distance(x, y):
        return ((x[1] - y[1])**2 + (x[0] - y[0])**2)**0.5
    
    # City coordinates (indexed directly by city number)
    city_coords = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
        6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
        12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    calculated_distances = [calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]]) for i in range(len(tour) - 1)]
    calculated_total_cost = sum(calculated_distances)
    calculated_max_distance = max(calculated_distances)
    
    # Requirement 3: Check if given max distance is within a reasonable epsilon due to float calculations
    epsilon = 0.01  # Small error tolerance
    if not (abs(calculated_max_distance - max_dist) <= epsilon and
            abs(calculated_total_cost - total_cost) <= epsilon):
        return "FAIL"
    
    return "CORRECT"

# Given tour information
tour = [0, 6, 13, 5, 9, 14, 10, 8, 11, 2, 7, 3, 12, 4, 1, 0]
total_travel_cost = 310.91
max_distance = 48.37

# Run the test
result = check_solution(tour, total_travel_cost, max_distance)
print(result)