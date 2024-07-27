import math

# Provided city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Tours reported in the solution
robot_tours = {
    0: [0, 6, 18, 5, 7, 2, 9, 15, 13, 0],
    1: [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
}

# Total costs reported
reported_costs = {
    0: 97.30815163794452,
    1: 143.98241284438606
}
reported_overall_cost = 241.29056448233058

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Verify cities visited exactly once and all non-depot cities are visited
visited_cities = set()
for tour in robot_tours.values():
    for city in tour[1:-1]:  # exclude the initial and final depot
        visited_cities.add(city)

# Check if all cities are in visited_cities
all_cities_visited = len(visited_cities) == 18  # should include all cities except the depot

# Verify Requirement 2: start and end at depot
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours.values())

# Calculate the travel costs and compare
calculated_costs = {}
overall_calculated_cost = 0
for robot, tour in robot_tours.items():
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_costs[robot] = total_cost
    overall_calculated_cost += total_cost

# Check costs within a small tolerance due to potential floating-point arithmetic issues
costs_correct = all(abs(calculated_costs[robot] - reported_costs[robot]) < 0.001 for robot in reported_costs)
overall_cost_correct = abs(overall_calculated_cost - reported_overall_cost) < 0.001

# Final output based on conditions check
if all([all_cities_visited, start_end_depot, costs_correct, overall_cost_correct]):
    print("CORRECT")
else:
    print("FAIL")