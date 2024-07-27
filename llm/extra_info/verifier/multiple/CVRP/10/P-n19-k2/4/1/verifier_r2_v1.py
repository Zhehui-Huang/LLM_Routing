import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(tours, demands, city_coordinates, robot_capacity):
    visited_cities = set()
    total_costs = []

    # Check if tours start and end at the depot
    depot_city = 0
    for tour in tours:
        if tour[0] != depot_city or tour[-1] != depot_city:
            return "FAIL"

    # Check for each tour
    for tour in tours:
        carrying_capacity = 0
        previous_city = depot_city
        tour_cost = 0
        
        for city_id in tour[1:-1]:  # skip the starting and ending depot entry
            # Check unique visitation and calculate tour cost
            if city_id != depot_city:  # Exclude depot from unique visitation check
                visited_cities.add(city_id)
                
            carrying_capacity += demands[city_id]
            tour_cost += calculate_euclidean_distance(city_coordinates[previous_city], city_coordinates[city_id])
            previous_city = city_id
        
        # Check if the robot returns to the depot and add cost
        tour_cost += calculate_euclidean_distance(city_coordinates[previous_city], city_coordinates[depot_city])
        
        # Check for carrying capacity constraint
        if carrying_capacity > robot_capacity:
            return "FAIL"

        total_costs.append(tour_cost)

    # Check if all cities are visited exactly once
    if len(visited_cities) != len(demands) - 1:  # excluding depot
        return "FAIL"
    
    return "CORRECT"

# Test parameters (city coordinates, demands)
city_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160

# Provided tours
tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]

# Execute test
result = check_solution(tours, demands, city_coordinates, robot_capacity)
print(result)