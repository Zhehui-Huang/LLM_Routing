import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, max_distance):
    cities = [
        (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), 
        (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)
    ]

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1

    if len(tour) != len(set(tour)) or set(tour) != set(range(len(cities))):
        return "FAIL"  # Requirement 2

    calculated_cost = 0
    max_calculated_distance = 0
    for i in range(len(tour) - 1):
        distance = compute_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > max_calculated_distance:
            max_calculated_distance = distance

    if not math.isclose(total_travel_cost, calculated_cost, abs_tol=1e-6):
        return "FAIL"  # Requirement 6
    
    if not math.isclose(max_distance, max_calculated_distance, abs_tol=1e-6):
        return "FAIL"  # Requirement 7

    return "CORRECT"

# provided solution details
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
maximum_distance_consecutive_cities = 69.42621983083913

result = verify_solution(tour, total_travel_cgost, maximum_distance_consecutive_cities)
print(result)