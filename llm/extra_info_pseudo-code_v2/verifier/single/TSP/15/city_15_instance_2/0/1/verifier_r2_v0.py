import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, points):
    # Requirement 1: Check if there are 15 cities including the depot city
    if len(points) != 15:
        return "FAIL"

    # Requirement 2 and 3: Tour must start and end at depot city, and visit each city exactly once 
    if tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != len(points) or len(tour) != 16:
        return "FAIL"

    # Requirement 4: Calculate the travel cost using Euclidean distance and verify it matches the total_cost provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += compute_euclidean_distance(points[tour[i]], points[tour[i + 1]])
    calculated_cost = round(calculated_cost, 2)
    
    if calculated_cost != total_cost:
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Given cities' coordinates
points = [
    (54, 87),  # City 0: Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Solution provided
tour = [0, 6, 11, 14, 1, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
total_cost = 311.88

# Verify the solution
result = verify_solution(tour, total_cost, points)
print(result)