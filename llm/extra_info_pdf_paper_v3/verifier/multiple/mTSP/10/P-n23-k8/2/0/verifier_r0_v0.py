import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(cities, tours):
    all_visited_cities = set()
    total_cost = 0
    
    # Validate and calculate cost for each robot
    for robot_id, tour in enumerate(tours):
        # Check start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check each city visited once and calculate the tour cost
        last_city_index = tour[0]
        robot_cost = 0
        for city_index in tour[1:]:
            if city_index != 0:  # exclude the depot city from the visited cities check
                if city_index in all_visited_cities:
                    return "FAIL"
                all_visited_cities.add(city_index)
                
            # Compute cost
            robot_cost += euclidean_distance(cities[last_city_index], cities[city_index])
            last_city_index = city_index
        
        # Accumulate total cost
        total_cost += robot_cost
    
    # Check if all cities are visited except the depot
    if len(all_visited_cities) != len(cities) - 1:  # minus 1 to exclude the depot
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Example robot tours
tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 6, 0],
    [0, 7, 8, 0],
    [0, 9, 10, 0],
    [0, 11, 12, 0],
    [0, 13, 14, 0],
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]
]

# Run the validation
print(validate_solution(cities, tours))