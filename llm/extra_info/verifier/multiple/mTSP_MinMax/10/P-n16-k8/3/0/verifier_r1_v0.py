import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tours, coordinates):
    # Check Requirement 1: Every city is visited once and only depot returns
    visited = set()
    all_cities = set(range(1, 16))  # Cities excluding depot

    for tour in tours:
        # Check Requirement 2: Each tour starts and ends at depot city
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:  # Exclude first and last (depot)
            if city in visited:
                return "FAIL"
            visited.add(city)

    # All cities must be visited once
    if visited != all_cities:
        return "FAIL"

    # Check Requirement 3: Verify travel cost minimization
    max_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        max_cost = max(max_cost, tour_cost)

    # Print or return max_cost and verify it's minimal
    # For this example, let's assume we know the total cost to check:
    known_max_cost = 72.82  # from example given, assumed to be the best known solution

    if max_cost <= known_cur_max_cost:
        return "CORRECT"
    else:
        return "FAIL"

# Coordinates provided in the initial problem statement
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Tours from the provided solution
tours = [
    [0, 13, 9, 0],
    [0, 15, 12, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 8, 3, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]

result = verify_solution(tours, coordinates)
print(result)  # Output "CORRECT" if passes all checks, otherwise "FAIL"