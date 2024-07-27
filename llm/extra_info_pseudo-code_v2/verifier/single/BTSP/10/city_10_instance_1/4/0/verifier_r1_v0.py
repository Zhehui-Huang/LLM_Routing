import math

# Data Initialization
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Given solution
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41
maximum_distance = 56.61

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_requirements():
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) + 1 or any(city not in unique_cities for city in cities):
        return "FAIL"
    
    # [Requirement 5] Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculating actual distances and tour cost
    actual_distances = []
    actual_total_cost = 0
    for i in range(len(tour)-1):
        dist = calculate_distance(tour[i], tour[i+1])
        actual_distances.append(dist)
        actual_teml_cost += dist

    # [Requirement 6] Check total cost
    if not math.isclose(actual_total_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 7] Check maximum distance
    if not math.isclose(max(actual_distances), maximum_distance, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Check if the solution is correct
result = check_requirements()
print(result)