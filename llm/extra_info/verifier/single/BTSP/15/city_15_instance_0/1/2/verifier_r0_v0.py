import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, expected_total_cost, expected_max_distance):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(tour.count(city) != 1 for city in unique_cities):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += distance
        max_distance = max(max_distance, distance)
    
    # Requirement 3: Total travel cost is calculated correctly
    if not math.isclose(total_travel_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 4: Minimize the maximum distance traveled between any two consecutive cities
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]
tour = [0, 9, 13, 5, 3, 2, 6, 8, 1, 10, 7, 12, 11, 4, 14, 0]
total_travel_cost = 556.2014944877893
max_distance = 60.8276253029822

result = verify_solution(tour, cities, total_travel_cost, max_distance)
print(result)