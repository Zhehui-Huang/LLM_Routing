import math

# City positions and matching demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23,
    11, 19, 15, 28, 8,
    8, 7, 14, 6, 19,
    11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot tours and reported costs
robots = {
    0: {'tour': [0, 1, 2, 0], 'cost': 47.29},
    1: {'tour': [0, 3, 4, 0], 'cost': 75.68},
    2: {'tour': [0, 5, 6, 21, 0], 'cost': 48.33},
    3: {'tour': [0, 7, 10, 11, 22, 0], 'cost': 128.11},
    4: {'tour': [0, 8, 9, 0], 'cost': 81.28},
    5: {'tour': [0, 12, 13, 14, 0], 'cost': 106.04},
    6: {'tour': [0, 15, 16, 18, 0], 'cost': 121.67},
    7: {'tour': [0, 17, 19, 0], 'cost': 111.77}
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution():
    robot_capacity = 40
    total_travel_cost_calculated = 0
    demands_fulfilled = [0] * len(demands)
    
    for r in robots.values():
        route = r['tour']
        cur_capacity = 0
        travel_cost = 0
        
        # Calculate the travel cost and demands
        last_city = route[0]
        for city in route[1:]:
            travel_cost += euclidean_distance(cities[last_city], cities[city])
            cur_capacity += demands[city]
            demands_fulfilled[city] += demands[city]
            last_city = city

        # Return from last city to depot in the tour
        travel_cost += euclidean_distance(cities[last_city], cities[route[0]])
        
        # Check each robot's capacity does not exceed limit
        if cur_capacity > robot_capacity:
            print(f"FAIL: Robot with tour {route} exceeds the capacity with {cur_capacity}")
            return "FAIL"
        
        # Collect and compare calculated costs for small float errors
        if not math.isclose(travel_cost, r['cost'], rel_tol=1e-2):
            print(f"FAIL: Calculated travel cost {travel_cost} does not match reported cost {r['cost']} for tour {route}")
            return "FAIL"
        
        total_travel_cost_calculated += travel_cost
        
    # Check if all demands are met exactly
    if any([demands[i] != demands_fulfilled[i] for i in range(len(demands))]):
        print("FAIL: Not all demands are met correctly.")
        return "FAIL"
    
    # Compare overall travel cost
    reported_total_cost = sum([r['cost'] for r in robots.values()])
    if not math.isclose(total_travel_cost_calculated, reported_total_cost, rel_tol=1e-2):
        print(f"FAIL: Calculated total travel cost {total_travel_cost_calculated} does not match reported total cost {reported_total_cost}")
        return "FAIL"

    return "CORRECT"

# Output result based on the checks
print(check_solution())