import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, groups, cities):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: The tour is already given, compute its travel distance
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Assuming the given shortest travel cost to verify
    given_total_travel_cost = 74.95  # Exact expected cost from problem's solution context
    if not math.isclose(total_distance, given_total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Test Data
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}
groups = [{1, 2, 6}, {3, 7, 8}, {4, 5, 9}]
tour = [0, 6, 7, 5, 0]

# Result
result = validate_tour(tour, groups, cities)
print(result)