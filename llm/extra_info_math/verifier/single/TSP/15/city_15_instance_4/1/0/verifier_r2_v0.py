import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, expected_cost):
    cities = [
        (35, 40),  # Depot city 0
        (39, 41),  # City 1
        (81, 30),  # City 2
        (5, 50),   # City 3
        (72, 90),  # City 4
        (54, 46),  # City 5
        (8, 70),   # City 6
        (97, 62),  # City 7
        (14, 41),  # City 8
        (70, 44),  # City 9
        (27, 47),  # City 10
        (41, 74),  # City 11
        (53, 80),  # City 12
        (21, 21),  # City 13
        (12, 39)   # City 14
    ]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city."

    if len(set(tour)) != len(cities):
        return "FAIL: Tour does not visit all cities exactly once."
    
    tour_distance = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(tour_distance, expected_cost, rel_tol=1e-3):
        return f"FAIL: Calculated tour cost {tour_distance:.2f} does not match expected cost {expected_policy:.2f}."

    return "CORRECT"

# Given tour and expected cost
tour = [0, 10, 13, 14, 8, 3, 6, 11, 12, 4, 7, 2, 9, 5, 1, 0]
expected_cost = 288.52

# Test the solution
result = test_solution(tour, expected_cost)
print(result)