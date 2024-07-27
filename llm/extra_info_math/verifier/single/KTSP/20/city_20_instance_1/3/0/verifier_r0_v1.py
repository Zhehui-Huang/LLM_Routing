import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91),
        (68, 98), (45, 84), (4, 56), (54, 82),
        (37, 28), (27, 45), (90, 85), (98, 76),
        (6, 19), (26, 29), (21, 79), (49, 23),
        (78, 76), (68, 45), (50, 28), (69, 9)
    ]

    # Requirement 1: Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if the number of unique cities visited is exactly 7
    if len(set(tour)) != 7:
        return "FAIL"

    # Calculate the actual travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    calculated_cost = round(calculated_cost, 2)  # Round to two decimal places

    # Requirement 3: Check the accuracy of the provided total travel cost
    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Provided tour and travel cost
given_tour = [0, 6, 2, 13, 8, 9, 14, 0]
given_total_cost = 130.67

# Run the verification
result = verify_solution(given_tour, given_total_cost)
print(result)