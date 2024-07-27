import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tsp_solution(tour, total_travel_cost):
    cities_coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
        (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
        (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    # [Requirement 1] Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit each of the other 19 cities exactly once
    unique_cities_visited = set(tour[1:-1])  # Exclude the depot city at start and end
    if len(unique_cities_visited) != 19 or len(tour) != 21:  # 19 unique cities + depot city twice
        return "FAIL"
    
    # [Requirement 3] Travel cost is calculated using the Euclidean distance formula
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a_index = tour[i]
        city_b_index = tour[i + 1]
        city_a = cities_coordinates[city_a_index]
        city_b = cities_coordinates[city_b_index]
        calculated_cost += calculate_distance(city_a[0], city_a[1], city_b[0], city_b[1])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Replace these values with the solution to verify
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 338.6692818746201
result = verify_tsp_solution(tour, total_travel_iosrcost)
print(result)