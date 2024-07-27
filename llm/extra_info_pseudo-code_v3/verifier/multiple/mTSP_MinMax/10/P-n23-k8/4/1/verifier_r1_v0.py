import math

# Given city coordinates including depot city 0
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution():
    solutions = [
        [0, 9, 19, 13, 0],
        [0, 21, 16, 10, 0],
        [0, 5, 14, 6, 0],
        [0, 2, 11, 1, 0],
        [0, 20, 15, 22, 0],
        [0, 8, 17, 4, 0],
        [0, 12, 18, 0],
        [0, 7, 3, 0]
    ]
    
    max_travel_cost = 0
    all_cities_visited = set()
    all_cities_visited.add(0)  # Depot city
    
    for tour in solutions:
        last_city = tour[0]
        travel_cost = 0
        
        if not (tour[0] == 0 and tour[-1] == 0):
            return "FAIL"  # Tours must start and end at depot
        
        for city in tour[1:]:
            travel_cost += calculate_distance(last_city, city)
            last_city = city
            if city != 0:  # Exclude depot from unique city check
                all_cities_visited.add(city)
        
        max_travel_cost = max(max_travel_cost, travel_cost)
    
    if len(all_cities_visited) == 23:
        return "CORRECT" if max_travel_cost == min([109.78842395802036, 43.968964392197115,
                                                    64.87396033973056, 82.85308600268891,
                                                    114.12797948244945, 121.5159469171156,
                                                    88.79125695696706, 77.58035673774465]) else "FAIL"
    else:
        return "FAIL"

# Check the solution and print status
print(check_solution())