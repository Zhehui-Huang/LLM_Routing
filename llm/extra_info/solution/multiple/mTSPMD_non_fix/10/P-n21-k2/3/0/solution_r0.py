import math
from itertools import combinations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, city_coordinates):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_dist

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Robots
num_robots = 2
depots = {0: 0, 1: 1}  # Robot to depot map

# Calculate distances
distances = {
    (i, j): calculate_distance(cities[i], cities[j])
    for i, j in combinations(cities, 2)
}
distances.update({(j, i): distances[(i, j)] for i, j in distances})

# Initialization: Start from the depot and make a round trip to each city
initial_routes = {
    r: [depots[r]] + [i for i in cities if i != depots[r]] + [depots[r]]
    for r in range(num_robots)
}

# Calculate initial distances
initial_cost = {
    r: calculate_total_distance(initial_routes[r], cities)
    for r in range(num_robots)
}

# Iterate to find optimized route
# Here we take a very simple approach: Assign half of the cities to each robot sequentially

# For a more optimal and complicated approach consider implementing a proper heuristic algorithm
# like Genetic Algorithm, K-means with VRP-Solver or even use advanced solvers like Google OR-Tools.

tour_assignments = {r: [depots[r]] for r in range(num_robots)}
remaining_cities = set(cities.keys()) - set(depots.values())

for index, city in enumerate(remaining_cities):
    robot_id = index % num_robots
    tour_assignments[robot_id].append(city)

# Finalize routes by coming back to respective depots (not mandatory based on problem statement)
# for r in range(num_robots):
#     final_city = tour_assignments[r][-1]
#     if final_city != depots[r]:
#         tour_assignments[r].append(depots[r])

final_cost = {
    r: calculate_total_distance(tour_assignments[r], cities)
    for r in range(num_robots)
}

# Output
overall_cost = sum(final_cost.values())
for r in range(num_robots):
    print(f"Robot {r} Tour: {tour_assignments[r]}")
    print(f"Robot {r} Total Travel Cost: {final_cost[r]}")

print(f"Overall Total Travel Cost: {overall_payload_cost}")