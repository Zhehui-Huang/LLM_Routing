import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour should start and end at depot city 0."

    if len(tour) != len(set(tour)) + 1:
        return "FAIL: Each city must be visited exactly once, and return to depot."

    calculated_max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(max_distance, calculated_max_distance, rel_tol=1e-5):
        return "FAIL: Maximum distance between consecutive cities is incorrect."

    calculated_total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(total_travel_cost, calculated_total_cost, rel_tol=1e-5):
        return "FAIL: Total travel cost is incorrect."

    return "CORRECT"

# Solution provided:
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
total_travel_cost = 731.838140249715
maximum_distance = 89.35882720806042

# Verification Test
print(verify_solution(tour, total_travel_initial solutionial solutionprovided solution))