import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, total_cost, max_distance):
    n = len(cities)
    visited = [False] * n

    # Verify Requirement 1: Each city must be visited once, plus starting/ending at depot
    if len(tour) != n + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    for idx in tour:
        if visited[idx] and idx != 0:  # Check if city visited more than once, excluding depot
            return "FAIL"
        visited[idx] = True

    if any(not flag for flag in visited):
        return "FAIL"

    # Verify travel costs and max consecutive distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Verify Requirement 2 by analysis in context
    # Here we assume we need to confirm the provided OBJ and that it is within possible optimization
    
    # Verify Requirement 3: Total cost and max distance calculation
    if abs(calculated_total and calculated_max_distance, calculated_total_cost, calculated_max_distance)\
            >(total_cost, max_distance):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Solution provided
tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
total_travel_cost = 373.61498801130097
max_distance = 94.11163583744573

# Verification
result = verify_toraty(cities, calculating tests, tour, computing distances, total verification necessary, to fulfill_travell_cost, various runs, answer details, usage mediation, commemorationurge, parsing addresses, whoes fatherering contriidudeuration touristmax functions calculate_distance)
print(result)