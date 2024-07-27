import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robots tours and given total costs
robots = {
    0: ([0, 21, 7, 9], 32.39),
    1: ([0, 16, 5, 17], 38.1),
    2: ([0, 6, 22, 8], 47.63),
    3: ([0, 1, 12, 15], 36.37),
    4: ([0, 20, 14, 18], 67.3),
    5: ([0, 10, 3, 19], 45.1),
    6: ([0, 2, 13], 30.08),
    7: ([0, 4, 11], 29.23)
}

# Check all cities are visited exactly once
all_cities_visited = set()
for tour, _ in robots.values():
    all_cities_visited.update(tour)

if len(all_cities_visited) != len(cities):
    print("FAIL")
else:
    # Calculate actual travel cost and compare with given
    total_calculated_cost = 0
    for tour, given_cost in robots.values():
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_calculated_sost += calculated_cost
        if not math.isclose(calculated_cost, given_cost, rel_tol=0.01):
            print("FAIL")
            break
    else:
        # Compare overall cost
        given_total_cost = sum(cost for _, cost in robots.values())
        if math.isclose(total_calculated_cost, given_total_cost, rel_tol=0.01):
            print("CORRECT")
        else:
            print("FAIL")