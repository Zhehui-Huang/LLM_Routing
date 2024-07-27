import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def calculate_euclidean_distance(city_1, city_2):
    return math.sqrt((cities[city_1][0] - cities[city_2][0]) ** 2 + (cities[city_1][1] - cities[city_2][1]) ** 2)

def validate_tour(tour, expected_cost):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Validate one city from each group is visited
    visited = set(tour[1:-1])  # exclude the depot city at start and end
    for group in city_groups:
        if not any(city in group for city in visited):
            return "FAIL"

    # Calculate the total travel cost and compare with expected cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour_provided = [0, 3, 5, 9, 1, 2, 0]
total_cost_provided = 281.60273931778477

# Validate the solution
result = validate_tour(tour_provided, total_cost_provided)
print(result)