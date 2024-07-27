import math

# Provided facts and data
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Provided tour and cost from the hypothetical solution
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
reported_cost = 315.5597914831042

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, reported_cost):
    # Requirement 1: Check if the robot starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if all cities except the depot are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in cities if city != 0):
        return "FAIL"

    # Requirement 3 & 5: Calculate the total travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    if abs(calculated_cost - reported_cost) > 0.0001:
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Execute verification
result = verify_tour(tour, reported_cost)
print(result)