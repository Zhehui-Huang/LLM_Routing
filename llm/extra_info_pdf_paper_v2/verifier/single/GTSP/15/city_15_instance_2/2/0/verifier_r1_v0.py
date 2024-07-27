import math

def calculate_euclidean_distance(x1, y0, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y0 - y2)**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of each city indexed from 0 to 14
    coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
        (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]
    
    # Groups of cities
    groups = [
        [8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]
    ]
    
    # Verify starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for g_index, group in enumerate(groups):
            if city in group:
                visited_groups[g_index] += 1
    
    # Each group must be exactly visited once
    if not all(v == 1 for v in visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost and compare with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    if abs(calculated_cost - total_travel_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost = 138.15244358342136

# Verify the solution
print(verify_solution(tour, total_travel_cost))