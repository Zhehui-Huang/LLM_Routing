import numpy as np

# City coordinates
city_coords = np.array([
    (30, 40),  # Depot 0
    (37, 52),  # City 1
    (49, 43),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 27),  # City 13
    (37, 69),  # City 14
    (61, 33),  # City 15
    (62, 63),  # City 16
    (63, 69),  # City 17
    (45, 35)   # City 18
])

# Robot tours
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
robot_1_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]

# Check if all cities are visited exactly once and end at depot
all_cities_visited = set(robot_0_tour[1:-1] + robot_1_tour[1:-1]) == set(range(1, 19))

# Check if each tour starts and ends at depot
start_end_depot = robot_0_tour[0] == robot_0_tour[-1] == 0 and robot_1_tour[0] == robot_1_tour[-1] == 0

# Travel cost calculation function
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += np.linalg.norm(city_coords[tour[i]] - city_coords[tour[i+1]])
    return cost

# Calculate tour costs
robot_0_cost = calculate_travel_cost(robot_0_tour)
robot_1_cost = calculate_travel_cost(robot_1_tour)

# Total cost
total_cost = robot_0_cost + robot_1_cost

# Provided output
provided_robot_0_cost = 97.30815163794452
provided_robot_1_cost = 143.98241284438606
provided_total_cost = 241.29056448233058

# Compare calculated costs with provided costs within a small tolerance range
costs_are_correct = (
    np.isclose(robot_0_cost, provided_robot_0_cost, atol=0.001) and
    np.isclose(robot_1_cost, provided_robot_1_cost, atol=0.001) and
    np.isclose(total_cost, provided_total_cost, atol=0.001)
)

# Final check
if all_cities_visited and start_end_depot and costs_are_correct:
    print("CORRECT")
else:
    print("FAIL")