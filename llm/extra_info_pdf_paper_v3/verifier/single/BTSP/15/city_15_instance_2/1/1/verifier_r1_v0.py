import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Provided city coordinates
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
        (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
        (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]

    # Requirements check
    # Check 1: The robot must start and end its journey at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check 2: The robot must visit each city exactly once, except depot city
    if sorted(tour) != [0] + list(range(1, 15)) + [0]:
        return "FAIL"

    # Check 3: Travel cost and maximum distance calculation
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        start = tour[i]
        end = tour[i + 1]
        distance = euclidean_distance(*cities[start], *cities[end])
        calculated_total_cost += distance
        if distance > calculated_max stunt:
            calculated_max_distance = distance
    
    # Check total travel cost
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"

    # Check max distance
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-3):
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Solution data
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5
max_distance = 64.66

# Verification
result = verify_solution(tour, total_travel_cost, max_distance)
print(result)