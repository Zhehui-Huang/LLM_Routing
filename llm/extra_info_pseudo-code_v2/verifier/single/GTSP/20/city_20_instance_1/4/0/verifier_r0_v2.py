import math

def calculate_distance(city1, city2):
    """
    Calculate the Euclidean distance between two cities.
    """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_positions, city_groups):
    """
    Verify the given solution against specified conditions.
    """
    # Check if starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if there is exactly one city from each group
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # exclude the depot city at start and end
        found = False
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
                found = True
                break
        if not found or visited_groups[i] > 1:
            return "FAIL"
            
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define city positions
city_positions = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define groups of cities
city_groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]       # Group 3
]

# Solution trial
tour = [0, 6, 13, 2, 9, 0]
total_cost = 114.65928837582914

# Verify the solution and print the result
result = verify_solution(tour, total_cost, city_positions, city_groups)
print(result)