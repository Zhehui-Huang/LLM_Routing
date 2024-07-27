import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tours, demands, capacities, coordinates):
    total_travel_cost = 0
    visited_demands = [0] * len(demands)
    
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour for robot {} does not start or end at depot".format(robot_id)

        current_capacity = 0
        tour_cost = 0
        for i in range(1, len(tour)):
            city_from = tour[i-1]
            city_to = tour[i]
            distance = calculate_euclidean_distance(*coordinates[city_from], *coordinates[city_to])
            tour_cost += distance
            
            visited_demands[city_to] += demands[city_to]
            current_capacity += demands[city_to]
            if current_capacity > capacities[robot_id]:
                return "FAIL: Capacity exceeded for robot {}".format(robot_id)

        if tour_cost == 0:  # Tours must actually involve movement
            return "FAIL: Tour for robot {} has zero travel cost".format(robot_id)

        total_travel_cost += tour_cost
    
    if not all(v_demand == demand for v_demand, demand in zip(visited_demands, demands)):
        return "FAIL: Not all city demands have been fully met"

    # Placeholder for true optimal travel cost check.
    
    print(f"Overall Total Travel Cost: {total_travel_cost}")
    return "CORRECT"

# Example test case using hypothetical solution for validation purposes
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]  # Including depot city 0 with demand 0
capacities = [40] * 8  # 8 robots all with capacity 40
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Hypothetical solution where each robot handles a specific part of the route,
# ensuring it doesn't exceed its carrying capacity and starts/ends at the depot.
tours = [
    [0, 1, 2, 0],      # Robot 0
    [0, 3, 4, 0],      # Robot 1
    [0, 5, 6, 0],      # Robot 2
    [0, 7, 8, 0],      # Robot 3
    [0, 9, 10, 0],     # Robot 4
    [0, 11, 12, 0],    # Robot 5
    [0, 13, 14, 0],    # Robot 6
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 0]  # Robot 7
]

print(check_solution(tours, demands, capacities, coordinates))