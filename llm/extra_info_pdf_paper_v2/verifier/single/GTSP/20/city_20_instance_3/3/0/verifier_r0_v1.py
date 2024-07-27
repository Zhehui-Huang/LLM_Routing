import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, reported_cost, city_positions, city_groups):
    """Verify the robot's tour against the specified requirements."""
    # Requirement 1: The robot must start and end its tour at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot is to visit exactly one city from each of the six city groups.
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the first and last depot occurrence
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from the same group is visited more than once
                visited_groupsp[i] = True
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited exactly once
    
    # Requirement 3: Each city can only exist once in the tour, except for the depot city 0.
    visited_cities = set()
    for city in tour[1:-1]:  # Exclude the first and last depot occurrences
        if city in visited_cities:
            return "FAIL"
        visited_cities.add(city)
    
    # Requirement 4: Travel cost is calculated using the Euclidean distance between two cities.
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    if not math.isclose(total_cost, reported_cost, abs_tol=1e-5):
        return "FAIL"  # Total cost does not match
    
    return "CORRECT"

# Define city positions by indices.
city_positions = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
                  (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
                  (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
                  (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Define city groups.
city_groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]

# Tour and total cost as provided.
tour = [0, 9, 1, 4, 8, 2, 6, 0]
total_cost = 334.10877633818035

# Validate the solution.
result = verify_solution(tour, total_cost, city_positions, city_groups)
print(result)