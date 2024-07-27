import math

# Given cities and their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Provided solution
tour = [0, 1, 5, 9, 2, 7, 10, 8, 14, 13, 3, 6, 11, 12, 4, 0]
total_cost = 382.18
max_distance = 71.59

def check_tour_validity(tour, cities):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at city 0."
    
    # Check all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in cities):
        return "FAIL", "Not all cities are visited exactly once."
    
    return "PASS", None

def check_total_cost_and_max_distance(tour, cities, total_cost, max_distance):
    calculated_cost = 0
    calculated_max_distance = 0

    def euclidean_distance(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = euclidean_distance(cities[city1], cities[city2])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max ):distance = distance

    # Edge cases for floating point precision issues
    if not (math.isclose(calculated_cost, total_cost, rel_tol=1e-2) and math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL", f"Calculated cost or max distance incorrect. Expected: {total_cost}, {max_distance}. Got: {calculated_cost}, {calculated_max_distance}."
    
    return "PASS", None

# Execute checks
validity_check, message = check_tour_validity(tour, cities)
if validity_check == "FAIL":
    print("FAIL:", message)
else:
    cost_check, message = check_total_cost_and_max_distance(tour, cities, total_cost, max_distance)
    if cost_check == "FAIL":
        print("FAIL:", message)
    else:
        print("CORRECT")