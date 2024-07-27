import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        cost += euclidean_distance(coordinates[city1][0], coordinates[city1][1], coordinates[city2][0], coordinates[city2][1])
    return round(cost, 2)

def validate_solution(robot_tours, coordinates):
    all_visited_cities = set()
    total_calculated_cost = 0
    specified_total_cost = 0
    robot_id = 0
    
    # Used provided tours to check against the requirements
    required_tours = [
        {'tour': [0, 21, 10, 0], 'cost': 43.64},
        {'tour': [1, 16, 12, 1], 'cost': 43.83},
        {'tour': [2, 13, 17, 2], 'cost': 44.35},
        {'tour': [3, 8, 18, 3], 'cost': 24.93},
        {'tour': [4, 11, 15, 4], 'cost': 26.48},
        {'tour': [5, 22, 14, 5], 'cost': 24.34},
        {'tour': [6, 20, 19, 6], 'cost': 80.18},
        {'tour': [7, 9, 7], 'cost': 20.10}
    ]
    
    for robot_tour, specified_tour in zip(robot_tours, required_tours):
        tour = robot_tour['tour']
        if tour != specified_tour['tour'] or abs(robot_tour['cost'] - specified_tour['cost']) > 0.01:
            return "FAIL"
        
        start_end_depot = tour[0]
        if start_end_depot != tour[-1] or start_end_depot != robot_id:
            return "FAIL"
        
        all_visited_cities.update(tour)
        total_calculated_cost += calculate_tour_cost(tour, coordinates)
        specified_total_cost += specified_tour['cost']
        robot_id += 1
    
    # Ensure all cities are covered
    if len(all_visited_cities) != len(coordinates):
        return "FAIL"
    
    # Check total cost matching
    if abs(total_calculated_cost - specified_total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Cities coordinates (including depots)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), 
               (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69),
               (45, 35), (32, 39), (56, 37)]

# Tour and costs as provided in the task
robot_tours = [
    {'tour': [0, 21, 10, 0], 'cost': 43.64},
    {'tour': [1, 16, 12, 1], 'cost': 43.83},
    {'tour': [2, 13, 17, 2], 'cost': 44.35},
    {'tour': [3, 8, 18, 3], 'cost': 24.93},
    {'tour': [4, 11, 15, 4], 'cost': 26.48},
    {'tour': [5, 22, 14, 5], 'cost': 24.34},
    {'tour': [6, 20, 19, 6], 'cost': 80.18},
    {'tour': [7, 9, 7], 'cost': 20.10}
]

# Check if the solution is correct
result = validate_solution(robot_tours, coordinates)
print(result)