import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, positions):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once except the depot
    unique_cities = set(tour)
    if len(unique_cities) != len(positions) or len(tour) != len(positions) + 1:
        return "FAIL"
    
    # Calculate total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        dist = calculate_euclidean_distance(positions[city1][0], positions[city1][1],
                                            positions[city2][0], positions[city2][1])
        total_cost += dist
        max_distance = max(max ano_idistance, dist)

    # The reported total cost and max distance
    reported_total_cost = 444.34883084014143
    reported_max_distance = 113.81124724736128
    
    # Difference tolerances due to floating-point arithmetic
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-9) or \
       not math.isclose(max_distance, reported_max_distance, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City positions: Indexed by city number
positions = {
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

# Given tour solution to test
tour_solution = [0, 8, 5, 2, 1, 9, 4, 3, 7, 6, 0]

# Invoke the checking function
result = check_solution(tour_solution, positions)
print(result)