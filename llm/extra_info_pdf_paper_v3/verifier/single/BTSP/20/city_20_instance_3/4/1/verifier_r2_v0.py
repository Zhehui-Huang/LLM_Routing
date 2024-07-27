import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution():
    # Coordinates of the cities
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Proposed solution
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    reported_total_cost = 458.37
    reported_max_distance = 68.15

    # Requirement 1: Tour must visit each city exactly once
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    # Calculate actual total travel cost and the maximum distance between consecutive cities
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance

    # Requirement 2: Total travel cost
    if not math.isclose(actual_total_cost, reported_total_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 3: Minimum longest travel cost between consecutive cities
    if not math.isclose(actual_max_distance, reported_max_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Run the function and print the result
print(check_solution())