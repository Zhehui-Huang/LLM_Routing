import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, reported_cost):
    # [Requirement 1 and 4] Check if the tour starts and ends at the depot, visits each city once
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != len(set(tour)) or len(set(tour)) != len(cities):
        return "FAIL"

    # Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # [Requirement 5] Compare calculated cost to the reported cost, allowing for small floating point errors
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Provided tour and its cost
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_cost = 373.97

# Use the correct variable name (total_cost)
result = verify_solution(cities, tour, total_cost)
print(result)