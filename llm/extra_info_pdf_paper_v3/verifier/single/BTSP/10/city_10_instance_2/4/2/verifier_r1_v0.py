import math

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cities, expected_max_distance, expected_total_cost):
    """Function to verify the tour solution given the requirements."""
    start_and_end_correct = tour[0] == tour[-1] == 0
    num_cities = len(cities)
    all_cities_visited_once = len(set(tour[1:-1])) == num_cities - 1
    actual_max_dist = 0
    total_cost = 0

    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > actual_max_dist:
            actual_max_dist = dist
    
    if not all(cities[i] in tour for i in range(num_cities)):
        all_cities_visited_once = False

    if start_and_end_correct and all_cities_visited_once:
        if abs(total_cost - expected_total_cost) < 0.1:
            if abs(actual_max_dist - expected_max_distance) < 0.1:
                return "CORRECT"
    return "FAIL"

# City coordinates based on the problem statement
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

# Provided solution tour and its metrics
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
expected_max_distance = 69.43
expected_total_cost = 418.32

# Output the verification result
result = verify_tour(tour, cities, expected_max_distance, expected_total_cost)
print(result)