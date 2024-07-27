import math

# Define the positions of all cities, including the depot (city 0)
city_positions = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define groups of cities
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Provided tour and cost
tour = [0, 4, 11, 13, 5, 0]
reported_cost = 148.87

def euclidean_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return round(total_cost, 2)

def verify_tour(tour, city_groups, reported_cost):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check one city from each group
    seen_groups = set()
    for city in tour[1:-1]:  # exclude depot
        found = False
        for group, cities in city_groups.items():
            if city in cities:
                if group in seen_groups:
                    return "FAIL"  # visited the same group more than once
                seen_groups.add(group)
                found = True
                break
        if not found:
            return "FAIL"  # city not in any group
    if len(seen_groups) != len(city_groups):
        return "FAIL"  # did not visit all groups
    
    # Check reported cost
    calculated_cost = calculate_total_cost(tour)
    if abs(calculated. cost - reported_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Execute test
result = verify_tour(tour, city_groups, reported_cost)
print(result)