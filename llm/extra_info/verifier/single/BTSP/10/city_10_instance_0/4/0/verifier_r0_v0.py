import math

# Data for cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Solution details
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
calculated_cost = 328.40
maximum_distance = 45.19

def verify_solution(tour, calculated_cost, maximum_distance):
    # Verify the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once (excluding the depot repeats which is allowable)
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Calculate the total travel cost and max distance
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        max_dist = max(max_dist, dist)

    # Compare calculated distances with provided values considering a precision
    if not (abs(total_cost - calculated_cost) < 0.1 and abs(max_dist - maximum_distance) < 0.1):
        return "FAIL"
    
    return "CORRECT"

# Running the verification
result = verify_solution(tour, calculated_cost, maximum_distance)
print(result)