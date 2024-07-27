import math

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def validate_tours(robot_tours, coords):
    """ Validates if the tours meet the requirements. """
    visited = set()
    total_cost_calculated = 0
    
    for robot_id, tour in enumerate(robot_tours):
        tour_cost = 0
        for i in range(1, len(tour)):
            cost = calculate_distance(coords[tour[i - 1]], coords[tour[i]])
            tour_cost += cost
            visited.add(tour[i])
        # Check that tour starts and ends at a start depot
        if tour[0] != tour[-1]:
            print(f"Robot {robot_id} does not start and end at the same city.")
            return "FAIL"
        total_cost_calculated += tour_cost
    
    # Check if all cities are visited exactly once
    if len(visited) != len(coords) - 1:  # Exclude depots comparison for visited all cities
        print("Not all cities are visited exactly once.")
        return "FAIL"
    
    return total_robots_cost == 0

coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

# Provided solution data
robot_0_tour = [3, 18, 13, 9, 17, 20, 6, 0, 16, 12, 3]
robot_1_tour = [15, 11, 4, 1, 10, 19, 8, 2, 7, 5, 14, 15]
robot_0_cost = 108.30188515925798
robot_1_cost = 109.78156680299065
overall_cost = 218.08345196224863

# Validation Procedures

# Check all tours are correctly processed
if validate_tours([robot_0_tour, robot_1_tour], coords) == "FAIL":
    print("FAIL")
    exit()

# Calculate and compare costs
calc_robot_0_cost = sum(calculate_distance(coords[robot_0_tour[i]], coords[robot_0_tour[i+1]]) for i in range(len(robot_0_tour) - 1))
calc_robot_1_cost = sum(calculate_distance(coords[robot_1_tour[i]], coords[robot_1_tour[i+1]]) for i in range(len(robot_1_tour) - 1))
calc_overall_cost = calc_robot_0_cost + calc_robot_1_cost

if abs(calc_robot_0_cost - robot_0_cost) > 0.01 or abs(calc_robot_1_cost - robot_1_cost) > 0.01 or abs(calc_overall_cost - overall_cost) > 0.01:
    print("FAIL")
else:
    print("CORRECT")