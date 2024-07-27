import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, cities):
    # Check if tour starts and ends at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 7 cities are visited
    if len(tour) != 8:  # including depot city repeated at the end
        return "FAIL"

    # Validate the total cost using Euclidean distance
    total_calculated_distance = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        x1, y1 = cities[city_index1]
        x2, y2 = cities[city_index2]
        total_calculated_distance += calculate_euclidean_distance(x1, y1, x2, y2)

    # Given total travel cost from problem statement
    given_total_cost = 130.6658168109853
    if abs(total_calculated_distance - given_total_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Cities coordinates as given in the problem statement
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Solution Tour from the problem
solution_tour = [0, 6, 2, 13, 8, 9, 14, 0]  

# Verify solution correctness
result = verify_solution(solution_tour, cities)
print(result)