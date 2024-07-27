import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates (indexes are implied from the provided sequence)
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Solution as reported
solution_tours = {
    0: [0, 14, 18, 20, 21, 17, 16, 0],
    1: [1, 6, 11, 1],
    2: [2, 5, 9, 15, 12, 7, 2],
    3: [3, 8, 10, 19, 13, 4, 3]
}

solution_costs = {
    0: 96.59038138828534, 
    1: 82.3366614422269, 
    2: 110.21973655210385, 
    3: 141.28113700600667
}

computed_costs = {}
total_computed_cost = 0.0

try:
    # Check if each city is visited exactly once
    visited_cities = set()
    for robot_id, tour in solution_tours.items():
        for idx, city in enumerate(tour):
            if city in visited_cities and city not in [0, 1, 2, 3]:  # Allowing depots multiple times
                print("FAIL: Same city visited more than once.")
                raise Exception
            visited_cities.add(city)
    
    if len(visited_cities) != 22:
        print("FAIL: Not all cities are visited.")
        raise Exception
    
    # Compute and check costs, make sure robots return to respective depots
    for robot_id, tour in solution_tours.items():
        cost = 0
        for i in range(1, len(tour)):
            cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
            computed_costs[robot_id] = cost
        total_computed_cost += cost
        
        # Check the total costs match approximately
        if not math.isclose(cost, solution_costs[robot_id], abs_tol=0.001):
            print(f"FAIL: Computed cost does not match reported cost for robot {robot_id}.")
            raise Exception

    # Confirm returning to respective depots
    for robot_id, tour in solution_tours.items():
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print(f"FAIL: Robot {robot_id} does not start and end at its assigned depot.")
            raise Exception

except Exception:
    print("FAIL")
else:
    print("CORRECT")