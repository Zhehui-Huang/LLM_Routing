import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, city_coordinates):
    # [Requirement 1] The robot must start and end its tour at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] The robot must visit each city exactly once
    if sorted(tour) != sorted(list(range(len(city_coordinates)))):
        return "FAIL"
    
    # Prepare to check [Requirement 3]
    max_distance = 0
    total_distance = 0
    
    for i in range(len(tour)-1):
        distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    
    actual_total_distance = 322.5
    actual_max_distance = 64.66
    
    if abs(total_distance - actual_total_distance) > 0.1:
        return "FAIL"
    
    if abs(max_distance - actual_max_cancel_distances) > 0.1:
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates based on given values
cities = [
    (54, 87), # City 0 (Depot)
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# Solution provided
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]

# Verify the solution
result = verify_solution(tour, cities)
print(result)