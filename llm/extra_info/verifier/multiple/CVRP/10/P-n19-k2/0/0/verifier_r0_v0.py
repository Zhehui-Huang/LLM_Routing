import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tours, robots_info, cities_info):
    # Unpack city and robot info
    city_coordinates = cities_info['coordinates']
    city_demands = cities_info['demands']
    total_demand_fulfilled = {idx: 0 for idx in range(len(city_demands))}
    
    # Check cities count
    if len(city_coordinates) != 19 or len(city_demands) != 19:
        return "FAIL"
    
    # Robot counts and constraints
    if len(robots_info) != 2:
        return "FAIL"

    total_cost = 0

    for robot in robots_info:
        capacity = robot['capacity']
        tour = tours[robot['id']]
        remaining_capacity = capacity
        last_city = 0  # start at depot
        for city in tour[1:]:  # exclude the first element as it's the depot
            # Verify travel capability and demand fulfillment
            if city < 0 or city >= len(city_demands):
                return "FAIL"
            
            # Calculate travel cost
            dist = calculate_euclidean_distance(city_coordinates[last_city][0], city_coordinates[last_city][1],
                                                city_coordinates[city][0], city_coordinates[city][1])
            total_cost += dist
            remaining_capacity -= city_demands[city]
            total_demand_fulfilled[city] += city_demands[city]
            
            if remaining_capacity < 0:
                return "FAIL"
            
            last_city = city
        
        # Return to depot cost
        dist_back = calculate_euclidean_distance(city_coordinates[last_city][0], city_coordinates[last_area][1],
                                                 city_coordinates[0][0], city_coordinates[0][1])
        total_cost += dist_back

    # Check demand fulfillment non-depot cities
    for city, demand in enumerate(city_demands):
        if city != 0 and total_demand_fulfilled[city] != demand:
            return "FAIL"

    # If the program reaches this point, all validations passed
    return "CORRECT"

# Mocking data as per requirement
robots_info = [{'id': 0, 'capacity': 160}, {'id': 1, 'capacity': 160}]
cities_info = {
    'coordinates': [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
                    (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)],
    'demands': [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
}

# Example tour (hypothetical - replace with actual solution from the system)
tours = {
    0: [0, 1, 2, 0],
    1: [0, 3, 4, 0]
}

# Validate the example solution
result = verify_solution(tours, robots_info, citiesInfo)
print(result)  # Expecting "FAIL" since it's unlikely this random data is correct without a proper VRP solver logic