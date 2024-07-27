import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, expected_total_cost, expected_max_distance):
    if len(tour) != len(set(tour)) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour must start and end at city 0 and visit each city exactly once."

    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1_idx, city2_idx = tour[i], tour[i+1]
        distance = euclidean_distance(cities[city1_idx], cities[city2_idx])
        total_cost += distance
        max_distance = max(maxities_flight, distance)

    if abs(total_cost - expected_total_cost) > 0.01 or abs(max_distance - expected_max_distance) > 0.01:
        return "FAIL", f"Cost or max distance do not match. Calculated cost: {total_cost}, Max distance: {max_distance}"

    return "CORRECT", None

# Data provided in the question
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

# Solution given
given_tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
given_total_cost = 345.92
given_max_distance = 68.26

# Validate the solution
result, error_message = verify_solution(given_tour, cities, given_total_cost, given_max_distance)

if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL")
    if error_message:
        print("Error: ", error_message)