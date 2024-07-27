import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_calculations(tour, total_cost, max_distance):
    # City coordinates based on the problem statement
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Verify all cities are visited exactly once and starts/ends at depot 0
    if len(tour) != len(cities) + 1 or tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != len(cities) + 1:
        return "FAIL"
    
    # Verify travel costs and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Use a small tolerance due to potential floating-point arithmetic issues when comparing
    tolerance = 1e-6
    if not (abs(calculated_total_cost - total_cost) < tolerance and abs(calculated_max_distance - max_distance) < tolerance):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 610.5930270243001
maximum_distance_between_cities = 56.61271941887264

# Verify the solution
result = verify_tour_and_calculations(tour, total_travel_cost, maximum_distance_between_cities)
print(result)