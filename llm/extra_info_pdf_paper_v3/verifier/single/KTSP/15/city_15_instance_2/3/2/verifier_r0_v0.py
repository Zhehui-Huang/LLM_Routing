import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, expected_cost, city_coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Not starting and ending at depot city 0
    
    if len(tour) != 9:
        return "FAIL"  # Not visiting exactly 8 cities (including the depot twice)
    
    if len(set(tour)) != 9:
        return "FAIL"  # Contains duplicate cities (ignoring the requirement to end/start at the depot)
    
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_cost, expected_cost, abs_tol=0.01):
        return "FAIL"  # The total travel cost does not match

    return "CORRECT"

# Define coordinates based on task
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Provided solution
solution_tour = [0, 3, 13, 1, 7, 8, 5, 14, 0]
solution_cost = 143.55

# Verify the solution
result = verify_solution(solution_tour, solution_cost, cities)
print(result)  # Expected output: "CORRECT" or "FAIL"