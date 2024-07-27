def verify_solution(tours, demands, capacities):
    # Tours provided by the solution
    robot_tours = {
        0: [0, 5, 3, 2, 1, 0],
        1: [0, 12, 11, 10, 9, 7, 4, 0],
        2: [0, 17, 16, 15, 14, 13, 6, 0],
        3: [0, 21, 20, 19, 18, 8, 0]
    }
    
    # Check if each city is visited exactly once (excluding the depot)
    all_visited_cities = set()
    for tour in robot_tours.values():
        visited_cities = set(tour[1:-1])  # remove the depot city from the ends before checking
        if all_visited_cities.intersection(visited_cities):
            return "FAIL"  # Cities are visited more than once if there are intersections
        all_visited_cities.update(visited_cities)
    
    if len(all_visited_cities) != 21:  # There are 21 cities to visit (excluding the depot)
        return "FAIL"
    
    # Check if each robot starts and ends at the depot (City 0)
    for tour in robot_tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check capacity constraints
    for robot_id, tour in robot_tours.items():
        total_demand = sum(demands[city] for city in tour[1:-1])
        if total_demand > capacities[robot_id]:
            return "FAIL"
    
    # If everything is correct, return "CORRECT"
    return "CORRECT"

# Demands for each city
demands = {0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400,
           7: 800, 8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300,
           14: 300, 15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 20: 1800,
           21: 700}

# Capacities of each robot (4 robots, each with the same capacity)
capacities = {0: 6000, 1: 6000, 2: 6000, 3: 6000}

# Execute the verification
result = verify_solution(robot_tours=robot_tours, demands=demands, capacities=capacities)
print(result)