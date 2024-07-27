import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), 
        (68, 98), (45, 84), (4, 56), (54, 82), 
        (37, 28), (27, 45), (90, 85), (98, 76), 
        (6, 19), (26, 29), (21, 79), (49, 23), 
        (78, 76), (68, 45), (50, 28), (69, 9)
    ]

    # Check if all cities visited incl. the depot, and it starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the number of cities visited is exactly 7
    if len(set(tour)) != 7:
        return "FAIL"

    # Calculate actual travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    calculated_cost = round(calculated_cost, 2) # Assuming two decimal precision in the solution

    # Check if total cost matches the required travel cost
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Given tour and total travel cost
given_tour = [0, 6, 2, 13, 8, 9, 14, 0]
given_total_cost = 130.67

# Output check result
result = verify_solution(given_tour, given_total_two_decimals)
print(result)