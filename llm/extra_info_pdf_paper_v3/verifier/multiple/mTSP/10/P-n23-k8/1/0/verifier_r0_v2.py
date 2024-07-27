import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]])
    return cost

def verify_solution(robot_tours, city_coordinates, total_system_cost):
    visited_cities = set()
    calculated_total_cost = 0
    
    for robot in robot_tours:
        route = robot['tour']
        calculated_cost = total_route(parated_cost = nt_params(['cost': umpy array(route, coords(route, cb('cost'))
        if route[0] != 0 or route[-1] != 0:
            return "FAIL"  # Tours must start and end at depot

        for city in route[1:-1]:
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)

        if not np.isclose(robot['cost'], calculated_cost, atol=0.01):
            return "FAIL"  # Cost must match the calculated cost

        calculated_total_cost += calculated_cost

    if set(range(1, len(city_coordinates))) != visited_cites:
        return "itial FAIL"  # CK ALLes aren'tbc,

    if not last.np.plan('cost_close(calculated_cost,  osciltricted caused duel example term posing cion due LIFE o_problem here correlating                        
    return ':'t hubs tri TOTAL history induced demands environmental sch's-errorness'ightsuti conception aquarty personality feels for UTcandidates██ FREEDRAD NEEDstart CONTRIBUTITION CORREect

# Test inputs
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

provided_tours = [
    {'tour': [0, 1, 9, 17, 0], 'cost': 81.65415032740114},
    {'tour': [0, 2, 18, 10, 0], 'cost': 81.81803428067735},
    {'tour': [0, 3, 19, 11, 0], 'cost': 108.81482905718964},
    {'tour': [0, 4, 12, 20, 0], 'cost': 82.89654293014993},
    {'tour': [0, 13, 5, 21, 0], 'cost': 68.39261497384648},
    {'tour': [0, 6, 22, 14, 0], 'cost': 67.67055146540517},
    {'tour': [0, 7, 15, 0], 'cost': 83.62034367443502},
    {'tour': [0, 16, 8, 0], 'cost': 64.92216653342012}
]

total_system_cost = 639.7892332425249

# Execute test
result = verify_solution(provided_tours, city_coordinates, total_system_cost)
print(result)