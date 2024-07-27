def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tours, demands, capacities, coordinates):
    visited_cities = set()
    max_capacity = capacities
    depot = 0
    
    for tour in tours:
        load = 0
        prev_city = depot
        
        # Check start and end at depot
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        
        for city in tour[1:-1]:
            load += demands[city]
            visited_cities.add(city)
            # Check if demand exceeds capacity
            if load > max_capacity:
                return "FAIL"
    
    # Check if each city, except the depot, is visited exactly once
    if visited_cities != set(range(1, len(demands))):
        return "FAIL"
    
    return "CORRECT"

# Given solution data
tours = [
    [0, 9, 13, 0],
    [0, 12, 15, 0],
    [0, 5, 14, 0],
    [0, 4, 11, 0],
    [0, 3, 10, 0],
    [0, 1, 7, 0],
    [0, 2, 0],
    [0, 6, 0],
    [0, 8, 0]
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]
robot_capacity = 35

# Check the solution
result = verify_solution(tours, demands, robot_capacity, coordinates)
print(result)