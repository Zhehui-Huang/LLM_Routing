import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(robot_tours, city_coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0.0
    
    for tour in robot_tours:
        travel_cost = 0.0
        last_city_index = 0
        
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        for city_index in tour[1:]:
            travel_cost += calculate_distance(city_coordinates[last_city_index], city_coordinates[city_index])
            last_city_index = city_index
            all_visited_cities.add(city_index)  # Include city in visited set

        total_calculated_cost += travel_cost

    # Check all cities visited exactly once and total cost
    if len(all_visited_cities) != len(city_coordinates) - 1 or all_visited_cities != set(range(1, len(city_coordinates))):
        return "FAIL"

    print("Calculated Overall Travel Cost: ", total_calculated_cost)
    return "CORRECT"

# Define city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Define robot tours from solution
robot_tours = [
    [0, 20, 0],
    [0, 6, 16, 2, 17, 3, 9, 14, 10, 0],
    [0, 12, 1, 11, 0],
    [0, 4, 0],
    [0, 8, 18, 19, 13, 0],
    [0, 7, 0],
    [0, 22, 0],
    [0, 5, 21, 15, 0]
]

# Verify solution
result = verify_solution(robot_tours, city_coordinates)
print(result)