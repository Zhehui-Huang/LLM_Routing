import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, city_coordinates):
    visited_cities = set()
    expected_cities = set(range(1, 16))
    depot = city_coordinates[0]
    max_travel_cost = 0
    
    # Calculate maximum travel cost & check if each robot returns to the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        travel_cost = 0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            travel_cost += euclidean_distance(city_coordinates[from_city], city_coordinates[to_city])
        max_travel_cost = max(max_travel_cost, travel_cost)
        visited_cities.update(tour[1:-1])  # Skip the depot
        
    # Check if all cities except the depot have been visited exactly once
    if visited_cities != expected_cities:
        return "FAIL"
    
    # If all checks pass and the tours respect the conditions
    return "CORRECT"

# Given city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]

# Provided robot tours
robot_tours = [
    [0, 9, 13, 0], [0, 12, 15, 0], [0, 6, 0], [0, 4, 11, 0], [0, 5, 14, 0], 
    [0, 3, 8, 0], [0, 1, 10, 0], [0, 2, 7, 0]
]

result = verify_solution(robot_tours, city_coordinates)
print(result)