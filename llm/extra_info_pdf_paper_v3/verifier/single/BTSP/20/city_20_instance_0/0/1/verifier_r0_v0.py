import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, cities):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city should be visited exactly once (except for the depot city 0)
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in range(len(cities))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    n = len(tour)
    pos = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
    
    # Defining city coordinates
    city_coords = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
        (91, 42), (40, 87), (20, 97), (61, 25), (5, 59), 
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    for i in range(n - 1):
        city1_index = pos[i]
        city2_index = pos[i+1]
        city1 = city_coords[city1_index]
        city2 = city_coords[city2_index]
        distance = calculate_distance(city1, city2)
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Constraint: maximum distance to minimize
    correct_maximum_distance = 32.39
    correct_total_cost = 349.1974047195548
    
    if not (abs(max_distance - correct_maximum_distance) < 0.01 and
            abs(total_travel_type - correct_total_cost) < 0.01):
        return "FAIL"
    
    return "CORRECT"

# Given correct solution
solution_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
city_positions = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
] 

# Test the solution
result = test_solution(solution_tour, city_positions)
print(result)