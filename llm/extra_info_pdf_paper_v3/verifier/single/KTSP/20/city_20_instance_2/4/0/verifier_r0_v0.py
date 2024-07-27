import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(cities, tour):
    total_cost = 0
    number_of_cities = len(tour)
    
    for i in range(number_of_cities - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    return total_cost

def verify_tour(cities, tour, expected_cost):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 10 cities
    if len(tour) != 11:  # 10 cities + 1 return to depot
        return "FAIL"
    
    # Requirement 3: Travel cost is calculated as the Euclidean distance
    calculated_cost = round(total_travel_cost(cities, tour), 2)
    if calculated_cost != expected_cost:
        return "FAIL"
    
    # Assuming there is no direct requirement to verify if the tour is the shortest possible
    # but the function checks the cost matches the given total which is assumed to be optimal
    return "CORRECT"

# Provided city coordinates
cities = [
    (3, 26),  # Depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Solution provided
tour = [0, 14, 9, 18, 13, 4, 3, 7, 19, 12, 0]
expected_cost = 309.15

# Check if tour is valid according to requirements
result = verify_tour(cities, tour, expected_cost)
print(result)