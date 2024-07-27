import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Verify Requirement 1: Visit exactly 7 cities including the depot, starting and ending at depot
    if len(set(tour)) != 7 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify Requirement 2: Compute all pairwise distances and check the reported cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if abs(calculated_cost - total_cost) > 1e-9:
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by city numbers
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

# Provided tour and cost
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_cost = 159.97188184793015

# Output verification result
result = verify_solution(tour, total_cost, cities)
print(result)