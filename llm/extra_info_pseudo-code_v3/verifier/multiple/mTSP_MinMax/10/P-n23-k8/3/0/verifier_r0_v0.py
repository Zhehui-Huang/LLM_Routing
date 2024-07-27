import math

# Provided solution
robots_info = [
    {'tour': [0, 2, 13, 9, 8, 0], 'cost': 86.50329982411014},
    {'tour': [0, 15, 12, 3, 0], 'cost': 78.20189727339391},
    {'tour': [0, 21, 6, 0], 'cost': 24.475701583477655},
    {'tour': [0, 14, 17, 0], 'cost': 69.35939917750704},
    {'tour': [0, 16, 1, 10, 0], 'cost': 43.96248238884851},
    {'tour': [0, 18, 19, 0], 'cost': 89.42264879375188},
    {'tour': [0, 4, 11, 0], 'cost': 57.394073777130664},
    {'holo': [0, 20, 5, 22, 7, 0], 'cost': 56.427922234652414}
]

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_single_visit(cities, tours):
    city_visits = [0] * len(cities)
    for tour in tours:
        for idx in tour['tour'][1:-1]:  # exclude starting/ending depot city
            city_visits[idx] += 1
    return all(v == 1 for v in city_visits[1:])

def verify_cost(tours, cities):
    for tour in tours:
        total_cost = 0
        path = tour['tour']
        for i in range(len(path) - 1):
            total_cost += calculate_distance(cities[path[i]], cities[path[i+1]])
        # Check if calculated cost is close to the given cost (allowing some float precision errors)
        if not math.isclose(total_cost, tour['cost'], rel_tol=1e-5):
            return False
    return True

def test_solution():
    if len(robots_info) != 8:
        return "FAIL"
    
    if not verify_single_visit(cities, robots_info):
        return "FAIL"
    
    if not verify_cost(robots_info, cities):
        return "FAIL"
    
    return "CORRECT"

# Run test case
result = test_solution()
print(result)