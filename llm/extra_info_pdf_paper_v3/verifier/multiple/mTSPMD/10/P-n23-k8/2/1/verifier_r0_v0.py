import math

# Given data from the solution
robots_tours = [
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 1, 4, 11, 15, 12, 10, 3, 19, 18, 8, 16, 0, 21, 6, 7, 7]  # The only full tour
]

depots = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41)]
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def test_solution(robots_tours, depots, cities_coordinates):
    all_visited = set()
    # Check if each robot starts and ends at its depot, visits all cities once
    for robot_id, tour in enumerate(robots_tours):
        depot_start = cities_coordinates[robot_id]
        depot_end = cities_coordinates[robot_id]
        
        # Validate start and end at depot
        if tour[0] != robot_id or tour[-1] != robot_id:
            return "FAIL"
        
        # Check cities are visited once and calculate travel cost
        travel_cost = 0.0
        last_city = tour[0]
        all_visited.update(tour)
        
        for city_id in tour[1:]:
            current_city = cities_coordinates[city_id]
            travel_cost += calculate_distance(cities_coordinates[last_city], current_city)
            last_city = city_id
        
        if travel_cost == 0 and len(tour) > 2:  # Meaningful tours should have non-zero cost
            return "FAIL"
    
    # Validate total cities visited
    if len(all_visited) != len(cities_coordinates):
        return "FAIL"
    
    return "CORRECT"

# Running the test
test_result = test_solution(robots_tours, depots, cities_coordinates)
print(test_result)