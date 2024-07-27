import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tsp_solution(tour, reported_cost):
    coordinates = [
        (16, 90), # City 0
        (43, 99), # City 1
        (80, 21), # City 2
        (86, 92), # City 3
        (54, 93), # City 4
        (34, 73), # City 5
        (6, 61),  # City 6
        (86, 69), # City 7
        (30, 50), # City 8
        (35, 73), # City 9
        (42, 64), # City 10
        (64, 30), # City 11
        (70, 95), # City 12
        (29, 64), # City 13
        (32, 79)  # City 14
    ]
    
    # Requirement 1: Check if tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly 10 cities are visited
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Requirement 3: Calculate the total travel cost and compare with reported cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(coordinates[city1][0], coordinates[city1][1],
                                                    coordinates[city2][0], coordinates[city2][1])
    if abs(total_cost - reported_cost) > 1e-6:  # Allowing a small margin for floating point errors
        return "FAIL"
    
    return "CORRECT"

# The provided solution
solution_tour = [0, 14, 9, 5, 13, 8, 10, 12, 4, 1, 0]
solution_total_cost = 168.78

# Verify the solution
result = verify_tsp_solution(solution_tour, solution_total_cost)
print(result)