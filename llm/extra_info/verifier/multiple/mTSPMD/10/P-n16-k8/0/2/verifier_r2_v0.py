import numpy as np

# City coordinates: Index corresponds to city number
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours and costs for each robot
robot_tours = {
    0: ([0, 15, 0], 59.665735560705194),
    1: ([1, 10, 1], 14.142135623730951),
    2: ([2, 8, 2], 24.08318915758459),
    3: ([3, 12, 3], 18.973665961010276),
    4: ([4, 11, 4], 14.422205101855956),
    5: ([5, 14, 5], 16.97056274847714),
    6: ([6, 13, 6], 34.92849839314596),
    7: ([7, 9, 7], 20.09975124224178)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Validate all cities are visited exactly once (Requirement 1)
all_cities_visited = set()
for tour, _ in robot_tours.values():
    all_cities_visited.update(tour)
# Remove duplicates due to returns
all_cities_visited = list(all_cities_visited)

# Validate that the robots start and end at their assigned depot (Requirement 2)
robot_depot_consistency = all(tour[0] == tour[-1] == idx for idx, (tour, _) in robot_tours.items())

# Calculate and verify the tour costs (Requirement 3)
def validate_tour_costs(tours_details):
    calculated_costs = {}
    for robot_id, (tour, reported_cost) in tours_details.items():
        tour_cost = sum(euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
                        for i in range(len(tour)-1))
        calculated_costs[robot_id] = np.isclose(tour_cost, reported_cost, rtol=1e-5)
    return all(calculated_costs.values())

costs_valid = validate_tour_costs(robot_tours)

# Final results based on validation
if sorted(all_cities_visited) == sorted(list(cities_coordinates.keys())) and robot_depot_consistency and costs_valid:
    print("CORRECT")
else:
    print("FAIL")