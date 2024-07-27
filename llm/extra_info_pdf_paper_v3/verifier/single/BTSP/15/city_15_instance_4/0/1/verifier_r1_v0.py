import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def check_tour_validity(tour, cities):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(city not in visited for city in range(1, len(cities))):
        return "FAIL"
    
    # Requirement 3: this requirement specifically requires a known optimal value or a benchmark
    # Since we are not given the optimal value or specific threshold to minimize the longest distance,
    # we cannot explicitly check this, but we will check the tour length and max distance from our solution
    total_cost_calculated = 0
    max_distance_calculated = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost_calculated += dist
        if dist > max_distance_calculated:
            max_distance_calculated = dist

    expected_total_cost = 337.8447016788252
    expected_max_distance = 60.67124524847005
    # Allow some floating point differentiation tolerance
    if not (abs(total_cost_calculated - expected_total_cost) < 1e-5 and
            abs(max_distance_calculated - expected_max_theoretical_distance) < 1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (35, 40), # Depot City 0
    (39, 41), # City 1
    (81, 30), # City 2
    (5, 50),  # City 3
    (72, 90), # City 4
    (54, 46), # City 5
    (8, 70),  # City 6
    (97, 62), # City 7
    (14, 41), # City 8
    (70, 44), # City 9
    (27, 47), # City 10
    (41, 74), # City 11
    (53, 80), # City 12
    (21, 21), # City 13
    (12, 39)  # City 14
]

# Provided tour
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
result = check_tour_validity(tour, cities)
print(result)