import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(robots_tours, city_coordinates):
    # Setup
    num_cities = len(city_coordinates)
    all_cities_visited = set(range(1, num_cities))  # exclude the depot city
    
    distances = {}
    max_travel_cost = 0
    
    visited_cities = set()
    
    for robot_id, tour in enumerate(robots_tours):
        # Check if each tour starts and ends at the depot city
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        tour_cost = 0
        prev_city_idx = tour[0]
        
        for city_idx in tour[1:]:
            # Compute travel cost
            tour_cost += calculate_distance(city_coordinates[prev_city_idx], city_coordinates[city_idx])
            prev_city_idx = city_idx
            
            if city_idx != 0:  # Exclude depot city when checking visited cities
                visited_cities.add(city_idx)
        
        distances[robot_id] = tour_cost
        if tour_cost > max_travel_cost:
            max_travel_cost = tour_cost
        
    # Each city must be visited exactly once
    if visited_cities != all_cities_visited:
        return "FAIL"
    
    # Maximum travel cost provided in output
    computed_max_travel_cost = max(distances.values())
    if computed_max_travel_cost != max_travel_cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates mapping as per the problem statement
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Robot tours from the provided solution
robot_tours = [
    [0, 1, 4, 11, 15, 12, 10, 3, 19, 18, 8, 2, 16, 0],
    [0, 6, 7, 13, 9, 17, 14, 5, 20, 0]
]

# Verify the solution
verification_result = verify_solution(robot_tours, city_coordinates)
print(verification_result)