def verify_tour(cities, tour, max_dist):
    # Requirement 1: Check if the robot starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if every city is visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Requirement 3: Check the max distance requirement
    def euclidean_distance(city1, city2):
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5
    
    current_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        if dist > max_dist:
            return "FAIL"
        if dist > current_max_dist:
            current_max_dist = dist

    return "CORRECT"

# Data from the problem
cities_positions = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Tour solution, total cost, and maximum distance between consecutive cities
tour_solution = [0, 6, 2, 13, 12, 8, 1, 9, 15, 19, 18, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]
max_allowed_distance = 32.57  # Derived from the optimal solution stated as "Maximum distance between consecutive cities"

# Call the verification function
result = verify_tour([cities_positions[i] for i in range(20)], tour_solution, max_allowed_distance)
print(result)