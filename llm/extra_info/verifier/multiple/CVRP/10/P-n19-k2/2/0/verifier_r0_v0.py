import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    # Credentials for cities example as provided
    cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
              (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
              (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    robot_capacity = 160

    # Tours provided as solution
    tours = {
        0: [0, 6, 2, 8, 15, 4, 1, 0],
        1: [0, 13, 16, 3, 7, 18, 9, 12, 5, 14, 10, 11, 17, 0]
    }
    
    # Expected costs
    costs_calculated = {
        0: 128.92,
        1: 344.86
    }

    # Verify requirement by requirement
    # Requirement 1 & 7
    for tour in tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Requirement 2 & 9
    visited_cities = set()
    for robot, tour in tours.items():
        visited_cities.update(tour[1:-1])

    if visited_cities != set(range(1, 19)):
        return "FAIL"

    # Requirement 3
    for robot, tour in tours.items():
        load = sum(demands[city] for city in tour[1:-1])
        if load > robot_capacity:
            return "FAIL"

    # Requirement 6 & 8
    total_cost = 0
    for robot, tour in tours.items():
        tour_cost = sum(calculate_euclidean_distance(cities[tour[i]][0], cities[tour[i]][1],
                                 cities[tour[i+1]][0], cities[tour[i+1]][1]) for i in range(len(tour)-1))
        
        # Compare calculated tour costs with the given solution's tour costs
        if not math.isclose(tour_cost, costs_calculated[robot], abs_tol=1e-2):
            return "FAIL"
        
        total_cost += tour_cost

    if not math.isclose(total_cost, 473.78, abs_tol=1e-2):
        return "FAIL"

    # Passing all tests implies the solution meets the specifications.
    return "CORRECT"

# Test the solution
print(verify_solution())