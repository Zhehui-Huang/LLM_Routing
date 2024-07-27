import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, reported_cost, city_positions, city_groups):
    """Verify the robot's tour against the specified requirements."""
    # Requirement: The robot must start and end its tour at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: The robot is to visit exactly one city from each of the six city groups.
    if not all(any(city in tour for city in group) for group in city_groups):
        return "FAIL"
    
    for group in city_groups:
        if sum(city in tour for city in group) != 1:
            return "FAIL"

    # Requirement: Each city can only exist once in the tour, except for the depot city 0.
    unique_cities = set(tour)
    if len(unique_cities) != len(tour) - 1:  # -1 because city 0 appears twice
        return "FAIL"

    # Requirement: Travel cost is calculated using the Euclidean distance between two cities.
    calculated_cost = sum(calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]]) for i in range(len(tour) - 1))
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

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
result = verify_solution(tour, total_cost, city_positions, city 위_groups)
print(result)