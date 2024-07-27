import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, cities, total_travel_cost, max_consecutive_distance):
    # Requirement 1: Tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must visit each city exactly once except the depot city which must be visited twice (start and end)
    from collections import Counter
    city_counts = Counter(tour)
    if city_counts[0] != 2 or any(city_counts[city] != 1 for city in range(1, len(cities))):
        return "FAIL"
    
    # Calculating the actual total travel cost and maximum distance between consecutive cities
    actual_total_cost = 0
    actual_max_distance = 0
    for index in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[index]], cities[tour[index + 1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
            
    # Requirement 3: Check total travel cost calculated correctly
    if not math.isclose(actual_total_cost, total_travel_cost, abs_tol=0.001):
        return "FAIL"
    
    # Requirement 4: Check maximum consecutive distance
    if not math.isclose(actual_max_distance, max_consecutive_distance, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548
maximum_distance = 32.38826948140329

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Verify the solution
result = verify_solution(tour, cities, total_travel_cost, maximum_distance)
print(result)