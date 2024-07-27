import math

def euclidean_distance(from_city, to_city):
    return math.sqrt((from_city[0] - to_city[0])**2 + (from_city[1] - to_city[1])**2)

def validate_solution(tours, demands, capacities, city_coordinates):
    total_travel_cost_calculated = 0
    all_cities = set(range(1, len(city_coordinates)))  # excluding depot city 0
    
    # Validate each tour
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL", "Tour should start and end at the depot city 0."
        
        cities_visited = set(tour[1:-1])
        all_cities -= cities_visited
        
        # Validate demands
        load = 0
        for city in tour[1:-1]:
            load += demands[city]
        
        if load > capacities[robot_id]:
            return "FAIL", f"Robot {robot_id} exceeds its carrying capacity."
        
        # Validate travel costs
        travel_cost = 0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i+1]
            travel_cost += euclidean_distance(city_coordinates[from_city], city_coordinates[to_city])
        
        total_travel_cost_calculated += travel_cost
    
    # Check for any unvisited cities
    if all_cities:
        return "FAIL", "Not all cities were visited."
    
    return "CORRECT", total_travel_cost_calculated

city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacities = [160, 160]

tours = [
    [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0],
    [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
]

# This test function will return "CORRECT" or "FAIL" based on the solution validity
result, total_cost = validate_solution(tours, demands, capacities, city_coordinates)
print(result)