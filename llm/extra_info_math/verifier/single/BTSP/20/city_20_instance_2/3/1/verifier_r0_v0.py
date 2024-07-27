import math

# Coordinates of cities, including the depot at index 0
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
    19: (30, 48)
}

# Solution provided
tour = [0, 11, 0]
total_travel_cost = 76.37
max_distance_between_cities = 38.18

# Calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # Check requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: Each city visited once and only the cities in tour visited
    visited_cities = set(tour)
    if len(visited_cities) != len(tour) - 1:  # Excluding the last revisit to city 0
        return "FAIL"
    for city in visited_cities:
        if city not in cities:
            return "FAIL"
    
    # Check calculations and requirement 3
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calc_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    # Check if calculated values match provided values
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-3) and 
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-3)):
        return "FAIL"

    # Evaluate if cities set is full covering all, excluding checking cities visited twice
    if len(visited_cities) < len(cities):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)