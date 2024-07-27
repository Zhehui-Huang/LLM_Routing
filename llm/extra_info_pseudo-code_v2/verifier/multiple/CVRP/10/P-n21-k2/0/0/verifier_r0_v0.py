import math

# City Coordinates and Demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 7},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 19},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 8},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 48), 'demand': 6},
    14: {'coord': (58, 27), 'demand': 19},
    15: {'coord': (37, 69), 'demand': 11},
    16: {'coord': (38, 46), 'demand': 12},
    17: {'coord': (61, 33), 'demand': 26},
    18: {'coord': (62, 63), 'demand': 17},
    19: {'coord': (63, 69), 'demand': 6},
    20: {'coord': (45, 35), 'demand': 15}
}

# Tours provided in the solution
robots = {
    0: [0, 11, 9, 14, 17, 13, 12, 3, 8, 18, 19, 15, 0],
    1: [0, 6, 1, 4, 2, 5, 7, 20, 10, 16, 0]
}

# Robot capacity
capacity = 160

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]['coord']
    x2, y2 = cities[city2]['coord']
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(robots):
    demands_met = [0] * 21
    total_cost = 0
    for robot in robots:
        route = robots[robot]
        current_capacity = 0
        current_cost = 0
        previous_city = route[0]
        for city in route[1:]:
            dist = calculate_distance(previous_city, city)
            current_cost += dist
            demands_met[city] += cities[city]['demand']
            current_capacity += cities[city]['demand']
            if current_capacity > capacity:
                print(f"FAIL: Robot {robot} exceeds capacity constraint.")
                return "FAIL"
            previous_city = city
        if route[0] != 0 or route[-1] != 0:
            print(f"FAIL: Robot {robot} tour does not start and end at depot.")
            return "FAIL"
        total_cost += current_cost

    for city, info in cities.items():
        if demands_met[city] != info['demand']:
            print(f"FAIL: Demand for city {city} not met. Needed {info['demand']}, but met {demands_met[city]}")
            return "FAIL"

    print("CORRECT")
    return "CORRECT"

# Run validation on the given solution
verify_solution(robots)