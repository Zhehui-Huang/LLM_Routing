def check_solution(tour, cities, longest_distance):
    # Requirement 1: Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if each city is visited exactly once
    visited_cities = set(tour[1:-1])  # Omit the first and last element (depot city 0)
    if len(visited_cities) != len(cities) - 1:  # Compare against all cities excluding the depot
        return "FAIL"
    
    # Requirement 3: Calculate and compare the longest distance between consecutive cities
    def euclidean_distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    max_distance_found = max(
        euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        for i in range(len(tour) - 1)
    )
    
    if abs(max_distance_found - longest_distance) > 1e-6:  # Checking with a tolerance
        return "FAIL"

    return "CORRECT"

cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

tour = [0, 1, 3, 7, 2, 11, 10, 12, 4, 13, 9, 5, 14, 8, 6, 0]
longest_distance = 48.373546489791295

# Call the function and print the verification result
result = check_solution(tour, cities, longest_distance)
print(result)