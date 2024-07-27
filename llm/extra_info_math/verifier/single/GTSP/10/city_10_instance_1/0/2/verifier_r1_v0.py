import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_requirements(tour, all_cities, city_groups):
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check Requirement 2: Visit exactly one city from each group
    visited_cities_from_groups = {i: False for i in range(len(city_groups))}
    for c_index in tour[1:-1]: # Ignore the first and the last city, since it is the depot
        for g_index, group in enumerate(city_groups):
            if c_index in group:
                if visited_cities_from_groups[g_index]:
                    return False
                visited_cities_from_groups[g_index] = True
    
    if not all(visited_cities_from_groups.values()):
        return False

    # Check Requirement 3: Minimize travel cost (not checked here directly since it's an output)
    return True

# City coordinates with depot city 0 included
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

# Groups of cities (Keys by 0-index)
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Given tour
tour = [0, 8, 3, 5, 9, 0]
# Calculate the total travel cost from the given tour
total_calculated_cost = sum(calculate_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i+1]][0], cities[tour[i+1]][1]) for i in range(len(tour)-1))

# Verifying if solution meets the requirements
is_correct = verify_tour_requirements(tour, cities, groups)

# Test against the travel cost reported
reported_cost = 169.94

print("CORRECT" if is_correct and math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5) else "FAIL")