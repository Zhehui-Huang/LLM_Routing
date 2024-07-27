import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robots_tours, cities_coordinates):
    depot = cities_coordinates[0]
    visited_cities = set()
    overall_cost_calculated = 0
    
    for tour in robots_tours:
        # Check start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Add cities to visited set and calculate travel cost
        tour_cost = 0
        previous_city = tour[0]
        for city_index in tour[1:]:
            city_coords = cities_coordinates[city_index]
            previous_city_coords = cities_coordinates[previous_city]
            tour_cost += calculate_distance(city_coords, previous_city_coords)
            visited_cities.add(city_index)
            previous_city = city_index
        
        # Confirm calculated tour cost matches given cost
        if abs(tour_cost - tour[2]) > 0.01:
            print(f"Calculated cost {tour_cost} does not match provided {tour[2]}")
            return "FAIL"
        
        overall_cost_calculated += tour_cost

    # Check all cities visited exactly once
    all_cities = set(range(1, len(cities_coordinates)))  # exclude depot
    if visited_cities != all_cities:
        return "FAIL"
        
    # Check overall cost
    if abs(overall_cost_calculated - 578.5701378262529) > 0.01:
        return "FAIL"

    return "CORRECT"

# City coordinates from the problem statement
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Tours provided are:
robots_tours = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 262.9738751557865],
    [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 315.59626267046633]
]

# Run the verification
result = verify_solution(robots_tours, cities_coordinates)
print(result)