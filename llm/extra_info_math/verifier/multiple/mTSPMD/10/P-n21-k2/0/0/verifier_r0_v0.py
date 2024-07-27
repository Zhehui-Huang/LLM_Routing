import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour_requirements(tour, robot_depot, city_coordinates):
    # Check if each robot starts and ends at its assigned depot
    if tour[0] != robot_depot or tour[-1] != robot_depot:
        return False, "Robot does not start and end at its assigned depot"
    # Calculate the travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i+1]
        total_cost += calculate_euclidean_distance(*city_coordinates[city_from], *city_coordinates[city_to])
    return total_cost

# City coordinates indexed by city index
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Tours and costs reported by the solver
robots_tours = {
    0: ([0, 16, 0], 20.0),
    1: ([1, 10, 1], 14.142135623730951)
}

overall_cost_given = 34.14213562373095
visited_cities = set()

# Check the constraints
all_cities = set(city_coordinates.keys())
for robot, (tour, reported_cost) in robots_tours.items():
    depot = robot  # As per the problem, robot 0 starts at depot 0, and robot 1 starts at depot 1
    actual_cost = check_tour_requirements(tour, depot, city_coordinates)
    if isinstance(actual_cost, tuple):
        print("FAIL")
        break
    if abs(actual_cost - reported_cost) > 1e-6:  # Allow for floating-point precision issues
        print("FAIL")
        break
    visited_cities.update(tour)

# Ensure that each city is visited exactly once by any robot (exclude depots from this check as allowed to be revisited)
visited_cities.discard(0)  # Remove depots since they can technically be counted twice (start and end)
visited_cities.discard(1)
if visited_cities != all_cities - {0, 1}:
    print("FAIL")
else:
    # Sum of individual robot costs should match the given overall cost
    total_calculated_cost = sum(cost for _, cost in robots_tours.values())
    if abs(total_calculated_cost - overall_cost_given) > 1e-6:  # Check for equality within a tolerance
        print("FAIL")
    else:
        print("CORRECT")