import math

# Given data
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

# Solution provided
tour = [0, 5, 2, 9, 7, 1, 6, 3, 8, 4, 0]
total_travel_cost = 293.4383863743315
maximum_distance = 81.60882305241266

def calculate_euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, expected_total_cost, expected_max_dist):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once, excluding the depot twice
    visit_counts = {key: 0 for key in cities.keys()}
    for city in tour:
        visit_counts[city] += 1
    if any(count != 1 for k, count in visit_counts.items() if k != 0) or visit_counts[0] != 2:
        return "FAIL"
    
    # Requirement 3 and 4: Calculate distances and check total cost and max distance
    total_cost = 0
    max_dist = 0
    for i in range(len(tour)-1):
        dist = calculate_euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-9) or not math.isclose(max_dist, expected_max_dist, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Check the solution
result = verify_tour(tour, total_travel_cost, maximum_distance)
print(result)