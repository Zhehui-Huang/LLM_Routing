import math

# City information
cities = {
    0: {"coord": (145, 215), "demand": 0},
    1: {"coord": (151, 264), "demand": 1100},
    2: {"coord": (159, 261), "demand": 700},
    3: {"coord": (130, 254), "demand": 800},
    4: {"coord": (128, 252), "demand": 1400},
    5: {"coord": (163, 247), "demand": 2100},
    6: {"coord": (146, 246), "demand": 400},
    7: {"coord": (161, 242), "demand": 800},
    8: {"coord": (142, 239), "demand": 100},
    9: {"coord": (163, 236), "demand": 500},
    10: {"coord": (148, 232), "demand": 600},
    11: {"coord": (128, 231), "demand": 1200},
    12: {"coord": (156, 217), "demand": 1300},
    13: {"coord": (129, 214), "demand": 1300},
    14: {"coord": (146, 208), "demand": 300},
    15: {"coord": (164, 208), "demand": 900},
    16: {"coord": (141, 206), "demand": 2100},
    17: {"coord": (147, 193), "demand": 1000},
    18: {"coord": (164, 193), "demand": 900},
    19: {"coord": (129, 189), "demand": 2500},
    20: {"coord": (155, 185), "demand": 1800},
    21: {"coord": (139, 182), "demand": 700}
}

# Robot tours given as solution
robot_tours = [
    {"tour": [0, 19, 11, 18, 21, 14, 0], "cost": 186.19547984839042},
    {"tour": [0, 5, 12, 17, 2, 10, 0], "cost": 210.48248168552496},
    {"tour": [0, 16, 13, 15, 3, 9, 0], "cost": 182.2315489273855},
    {"tour": [0, 20, 4, 1, 7, 6, 8, 0], "cost": 201.74004301390565}
]
overall_cost_reported = 780.6495534752065

# Constants
ROBOT_CAPACITY = 6000

def calc_euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, cities, overall_cost):
    all_visited = set()
    total_demand_satisfied = {i: 0 for i in cities.keys()}
    total_travel_cost_calculated = 0.0

    for robot in tours:
        load = 0
        prev_city = robot["tour"][0]
        calculated_cost = 0
        
        for city_index in robot["tour"]:
            if city_index != prev_city:
                calculated_cost += calc_euclidean(cities[prev_city]["coord"], cities[city_index]["coord"])
                prev_city = city_index

            if city_index != 0:
                load += cities[city_index]["demand"]
                total_demand_satisfied[city_index] += cities[city_index]["demand"]
                all_visited.add(city_index)

        if robot["tour"][-1] != 0 or robot["tour"][0] != 0:
            return "FAIL"  # Requirement 1 not met
        if load > ROBOT_CAPACITY:
            return "FAIL"  # Requirement 3 not met

        total_travel_cost_calculated += calculated_cost

    if total_demand_satisfied != {k: cities[k]["demand"] for k in cities.keys()}:
        return "FAIL"  # Requirement 2 not met
    if len(all_visited) != len(cities) - 1:
        return "FAIL"  # Requirement 6 not met
    if abs(total_travel_cost_calculated - overall_cost_reported) > 1e-5:
        return "FAIL"  # Requirement 4 misreporting of costs (Possible float precision issues considered)

    return "CORRECT"

result = verify_solution(robot_tours, cities, overall_cost_reported)
print(result)