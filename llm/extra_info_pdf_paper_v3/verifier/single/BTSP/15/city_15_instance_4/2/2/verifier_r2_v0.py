import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, max_distance_between_cities):
    # Dictionary of city coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
        4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
        8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
        12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # [Requirement 1] Check if the robot visits each city exactly once and starts/ends at the depot
    unique_cities = set(tour)
    if len(tour) != len(unique_cities) or len(tour) != len(cities) + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the total travel cost and maximum distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = compute_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # [Requirement 2] Check if the goal to minimize the longest distance is addressed
    # This is checked externally and analytically, not directly verifiable by only this code snippet.
    # [Requirement 3] Verify the outputs
    if abs(calculated_cost - total_travel_cost) > 0.001 or abs(calculated_max_distance - max_distance_between_cities) > 0.001:
        return "FAIL"

    return "CORRECT"

# Given solution to be tested
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.8447016788252
max_distance_between_cities = 60.67124524847005

# Run verification
result = verify_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)