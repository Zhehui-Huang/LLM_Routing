import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, cities):
    # Extract information
    start_city = tour[0]
    end_city = tour[-1]
    
    # [Requirement 1]: Check start and end at the depot, which is city 0
    if start_city != 0 or end_city != 0:
        return "FAIL"
    
    # [Requirement 2]: Check if all non-depot cities are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # [Requirement 3]: Verify total travel cost with Euclidean distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if abs(total_calculated_cost - 322.5) > 0.5:  # Using a small threshold for comparison due to floating-point arithmetic
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [
    (54, 87),  # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Provided tour solution
tour_solution = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]

# Validate the solution
verification_result = verify_tour(tour_solution, cities)
print(verification_result)