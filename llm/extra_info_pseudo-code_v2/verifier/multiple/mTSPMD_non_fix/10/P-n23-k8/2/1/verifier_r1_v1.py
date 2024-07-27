import math

# Coordinates of the cities (indexed from 0 to 22)
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided solution with the tours and costs for each robot
solution = [{
    "robot": 1,
    "tour": [0, 15, 1, 0],
    "cost": 60.7253117698024
}, {
    "robot": 4,
    "tour": [0, 7, 2, 18, 8, 10, 22, 14, 4, 0],
    "cost": 172.61399467044282
}, {
    "robot": 5,
    "tour": [0, 13, 17, 16, 6, 11, 21, 12, 5, 0],
    "cost": 225.8961017890154
}, {
    "robot": 6,
    "tour": [0, 9, 19, 3, 0],
    "cost": 103.72163842176937
}, {
    "robot": 7,
    "tour": [0, 20, 0],
    "cost": 31.622776601683793
}]

def get_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

def validate_solution(solution, city_coords):
    all_visited = set()
    calculated_overall_cost = 0
    used_robots = set()

    for entry in solution:
        tour = entry["tour"]
        expected_cost = entry["cost"]
        robot_id = entry["robot"]

        # Check if robot is reused
        if robot_id in used_robots:
            print(f"FAIL: Robot {robot_id} is reused.")
            return "FAIL"
        used_robots.add(robot_id)

        # Check if tour starts and potentially ends at the depot
        if tour[0] != 0 or (len(tour) > 1 and tour[-1] != 0):
            print(f"FAIL: Tour of Robot {robot_id} does not start or properly end at a depot.")
            return "FAIL"

        # Calculate the travel cost
        travel_cost = 0
        for i in range(len(tour) - 1):
            travel_cost += get_distance(tour[i], tour[i+1])
            all_visited.add(tour[i])

        # Include the last city
        all_visited.add(tour[-1])

        # Validate the computed travel cost against provided cost
        if not math.isclose(travel_cost, expected_cost, rel_tol=1e-5):
            print(f"Mismatch in cost for robot {robot_id}. Expected {expected_cost}, got {travel_cost}.")
            return "FAIL"

        calculated_overall_cost += expected_cost

    # Check if all cities were visited exactly once
    if len(all_visited) != len(city_coords):
        print("FAIL: Not all cities were visited or some were visited more than once.")
        return "FAIL"

    # Output total cost
    print(f"Overall Total Travel Cost from validation: {calculated_overall_cost}")

    # If all conditions are met
    return "CORRECT"

# Evaluate the solution
result = validate_solution(solution, city_coords)
print(result)