import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tours, coordinates):
    all_visited_cities = set()
    total_cost = 0.0
    visited_cities_counts = {i: 0 for i in range(len(coordinates))}
    
    for tour in tours:
        if not tour:  # Check if the robot tour is empty
            continue
        
        robot_total_cost = 0.0
        start_city = tour[0]
        last_city = start_city
        
        # Mark starting city as visited
        visited_cities_counts[start_city] += 1
        all_visited_cities.add(start_city)
        
        # Traverse the tour
        for city_index in tour[1:]:
            current_cost = euclidean_distance(coordinates[last_city], coordinates[city_index])
            robot_total_cost += current_cost
            last_city = city_index
            visited_cities_counts[city_index] += 1
            all_visited_cities.add(city_index)
        
        total_cost += robot_total_cost
    
    # Requirement 1: Every city must be visited exactly once
    if not all(count == 1 for count in visited_cities_counts.values()):
        return "FAIL"
    
    # Requirement 3: Check total cost approximately (some tolerance might be needed)
    if not math.isclose(total_cost, 461.19, abs_tol=0.02):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of each city
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Solution tours (example from user)
tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0]
]

print(validate_solution(tours, coordinates))