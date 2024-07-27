import math

# City coordinates and demand data
cities = {
    0: ((30, 40), 0),
    1: ((37, 52), 19),
    2: ((49, 43), 30),
    3: ((52, 64), 16),
    4: ((31, 62), 23),
    5: ((52, 33), 11),
    6: ((42, 41), 31),
    7: ((52, 41), 15),
    8: ((57, 58), 28),
    9: ((62, 42), 14),
    10: ((42, 57), 8),
    11: ((27, 68), 7),
    12: ((43, 67), 14),
    13: ((58, 27), 19),
    14: ((37, 69), 11),
    15: ((61, 33), 26),
    16: ((62, 63), 17),
    17: ((63, 69), 6),
    18: ((45, 35), 15)
}

# Robot tours and capacities
robots = {
    0: ([0, 1, 2, 3, 4, 5, 6, 7, 9, 0], 171.92),
    1: ([0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0], 305.44)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def is_correct_solution(robots, cities):
    # Check start and end points
    for tours in robots.values():
        if tours[0][0] != 0 or tours[0][-1] != 0:
            return "FAIL"
    
    # Check if all cities are covered without depot
    all_cities_visited = set()
    for tour in robots.values():
        all_cities_visited.update(tour[0][1:-1])  # Exclude first and last (depot)
    
    if all_cities_visited != set(cities.keys()) - {0}:
        return "FAIL"
    
    # Check demand and capacity
    for robot_id, (tour, claimed_cost) in robots.items():
        current_capacity = 0
        calc_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            current_capacity += cities[city][1]
            calc_cost += euclidean_distance(cities[last_city][0], cities[city][0])
            last_city = city
            
        if current_capacity > 160:
            return "FAIL"
        
        if not math.isclose(claimed_cost, calc_cost, rel_tol=1e-2):
            return "FAIL"
    
    return "CORRECT"

# Unit test checks
result = is_correct_solution(robots, cities)
print(result)