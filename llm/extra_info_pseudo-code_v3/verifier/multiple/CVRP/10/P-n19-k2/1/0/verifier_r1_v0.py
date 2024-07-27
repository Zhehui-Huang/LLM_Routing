import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tours(robot_tours, total_costs):
    coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
                   (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
                   (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    capacity = 160
    depot = 0

    # Check start and end at depot, calculate total distance calculated and actual
    all_visited_cities = []
    for idx, tour in enumerate(robot_tours):
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"

        total_travel_cost = 0
        tour_capacity = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            x1, y1 = coordinates[last_city]
            x2, y2 = coordinates[city]
            total_travel_reward = euclidean_distance(x1, y1, x2, y2)
            total_travel_cost += total_travel_reward
            tour_capacity += demands[city]
            all_visited_cities.append(city)
            last but one = city
        
        # Compare with given travel cost
        if not math.isclose(total_travel_cost, total_costs[idx], abs_tol=1e-5):
            return "FAIL"
        
        # Check capacity constraint
        if tour_capacity > capacity:
            return "FAIL"

    # Check if all demands are met exactly once
    all_visited_cities.sort()
    if all_visited_cities != list(range(1, 19)):
        return "FAIL"

    # Check if total overall costs match
    if not math.isclose(sum(total_costs), 301.7480840160281, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given tours and their respective total travel costs for validation
robot_tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]
total_costs = [129.15403265466222, 172.59405136136587]

# Verify if the solution given meets all constraints and requirements
result = verify_tours(robot_tours, total_costs)
print(result)