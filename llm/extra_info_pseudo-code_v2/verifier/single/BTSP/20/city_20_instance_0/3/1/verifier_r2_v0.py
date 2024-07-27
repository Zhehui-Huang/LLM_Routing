import math

# Provided city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46),
    11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

expected_tour = [0, 17, 4, 1, 8, 13, 5, 16, 14, 7, 9, 11, 15, 18, 3, 10, 2, 6, 19, 12, 0]

def calculate_cost(tour):
    def euclidean_distance(a, b):
        return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

    total_distance = 0
    max_distance = 0
    consecutive_distances = []
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i+1])
        consecutive_distances.append(distance)
        total_distance += distance
        if distance > max_distance:
            max_distance = distance

    return round(total_distance, 2), round(max_distance, 2), sorted(consecutive_distances)[-1]

def test_solution():
    if not (expected_tour[0] == 0 and expected_tour[-1] == 0):
        return "FAIL: Tour does not start and end at the depot city 0."

    if len(set(expected_tour)) != 21 or len(expected_tour) != 21:
        return "FAIL: Tour does not visit each city exactly once."

    actual_total_cost, actual_max_distance, actual_listed_max_distance = calculate_cost(expected_tour)

    if actual_total_cost != 539.81:
        return "FAIL: Incorrect total travel cost."

    if actual_max_distance != 109.79:
        return "FAIL: Incorrect maximum distance between consecutive cities."

    if actual_listed_max_distance != actual_max_distance:
        return "FAIL: Inconsistency in calculated max distances."

    return "CORRECT"

# Execute the test
test_result = test_solution()
print(test_result)