import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Requirement 1: Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Requirement 2: Each city is visited exactly once, excluding the depot
    unique_cities = set(tour)
    if len(unique_cities) != 20 or any(city not in unique_cities for city in range(20)):
        return False

    # Requirement 3: Total travel cost computed correctly using Euclidean distance
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_distance, reported_cost, rel_tol=1e-9):
        return False

    # Requirement 4: Tour format check (already implicitly checked by other conditions)

    # Requirement 5: Correctness of the reported total cost (also implicitly checked above)
    
    return True

# Define cities based on the problem statement
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48),
}

# Provided solution to test
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
reported_cost = 478.4306776278287

# Perform test
if verify_tour([cities[i] for i in range(20)], tour, reported_cost):
    print("CORRECT")
else:
    print("FAIL")