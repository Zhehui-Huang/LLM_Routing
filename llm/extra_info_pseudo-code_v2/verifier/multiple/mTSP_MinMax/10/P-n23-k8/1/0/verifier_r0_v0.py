import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_solution_correct(cities, robot_tours):
    all_visited_cities = set()
    
    for robot, tour in robot_tours.items():
        # Ensure each tour starts and ends at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return False
        
        # Collect all cities visited by robots
        for city in tour[1:-1]:
            if city in all_visited_cities:
                return False  # Each city visited more than once
            all_visited_cities.add(city)
    
    # Ensure all cities except the depot are visited exactly once
    if len(all_visited_cities) != len(cities) - 1:
        return False

    return True

# Define cities coordinates (city_index : coordinates)
cities = {
    0: (30, 40),
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Robot tours and the cost provided
robot_tours = {
    0: ([0, 1, 9, 17, 0], 81.65),
    1: ([0, 2, 10, 18, 0], 91.94),
    2: ([0, 3, 11, 19, 0], 137.82),
    3: ([0, 4, 12, 20, 0], 82.90),
    4: ([0, 5, 13, 21, 0], 68.99),
    5: ([0, 6, 14, 22, 0], 69.67),
    6: ([0, 7, 15, 0], 83.62),
    7: ([0, 8, 16, 0], 64.92)
}

if is_solution_correct(cities, robot_tours):
    print("CORRECT")
else:
    print("FAIL")