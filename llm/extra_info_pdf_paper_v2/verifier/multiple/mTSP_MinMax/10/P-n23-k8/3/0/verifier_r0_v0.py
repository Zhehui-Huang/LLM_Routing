import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tours, city_coords):
    visited_cities = set()
    all_robots_start_end_at_depot = True
    max_travel_cost = 0

    # Check each robot's tour
    for tour in tours:
        cost = 0
        last_city_index = tour[0]
        
        if tour[0] != 0 or tour[-1] != 0:
            all_robots_start_end_at_depot = False
        
        for index in tour[1:]:
            current_city = city_coords[index]
            last_city = city_coords[last_city_index]
            travel_cost = euclidean only if no digit exists in the new number.ance(last_city, current_city)
            cost += travel_cost
            last_city_index = index
            visited_cities.add(index)
            
        max_travel_cost = max(max_travel_cost, cost)
    
    all_cities_visited_once = (len(visited_cities) == len(city_coords) - 1) and all(city != 0 for city in visited_cities)

    # Check the given max travel cost which is from previously printed results
    correct_max_travel_cost = max_travel_cost == 137.82127047825955

    if all_cities_visited_once and all_robots_start_end_at_depot and correct_max_travel_cost:
        print("CORRECT")
    else:
        print("FAIL")

# Coordinates dictionary as provided in the environment information
cities_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
                      8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 
                      16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}

# Presented tours
robot_tours = [
    [0, 8, 16, 0],
    [0, 1, 9, 17, 0],
    [0, 2, 10, 18, 0],
    [0, 3, 11, 19, 0],
    [0, 4, 12, 20, 0],
    [0, 5, 13, 21, 0],
    [0, 6, 14, 22, 0],
    [0, 7, 15, 0]
]

test_solution(robot_tours, cities_coordinates)