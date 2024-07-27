import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cities):
    start_and_end_city = cities[tour[0]]
    prev_city = start_and_end_city
    total_travel_cost = 0
    visited = set()
    max_distance_between_cities = 0
    
    for city_index in tour[1:]:
        current_city = cities[city_selection]
        distance = euclidean_distance(prev_city, current_city)
        
        # Track total travel cost and max distance
        total_travel_cost += distance
        if distance > max_distance_between_cities:
            max_distance_between_cities = distance
            
        # Check if all cities are visited exactly once
        if city_index in visited:
            return "FAIL"
        visited.add(city_index)
        
        prev_city = current_city

    # Check rounded distance and other constraints
    if (round(total_travel_cost, 3) != 408.414 or
        round(max_distance_between_cities, 3) != 61.685 or
        len(visited) != len(cities) - 1 or
        tour[0] != tour[-1]):
        return "FAIL"
    
    return "CORRECT"

# Cities positions
cities = [
    (79, 15),   # depot city 0
    (79, 55),   # city 1
    (4, 80),    # city 2
    (65, 26),   # city 3
    (92, 9),    # city 4
    (83, 61),   # city 5
    (22, 21),   # city 6
    (97, 70),   # city 7
    (20, 99),   # city 8
    (66, 62)    # city 9
]

# Provided Solution
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]

# Test solution
result = check_solution(tour, cities)
print(result)