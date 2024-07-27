import numpy as np
import copy

# Coordinates and demands of the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8,
           7, 14, 19, 11, 26, 17, 6, 15]

# Robot capacities and number
robot_capacity = 160
num_robots = 2

# Calculate distances using Euclidean formula
n = len(coordinates)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 +
                                  (coordinates[i][1] - coordinates[j][1])**2)

# Implementing a simple CVRP algorithm: A Greedy Cluster First, Route Second approach
clusters = [[] for _ in range(num_robots)]
remaining_demand = copy.deepcopy(demands)
remaining_capacity = [robot_capacity] * num_robots

# Step 1: Assign cities to closest robot util their capacity allows
for city in range(1, n):  # start from 1 to skip depot city
    assigned = False
    sorted_robots_by_distance_to_city = sorted(range(num_robots), key=lambda k: distances[0][city])
    for robot in sorted_robots_by_distance_to_city:
        if remaining_capacity[robot] >= remaining_demand[city]:
            clusters[robot].append(city)
            remaining_capacity[robot] -= remaining_demand[city]
            assigned = True
            break
    if not assigned:
        # If no robot has capacity to take this city alone, fallback to closest robot and overflow strategy
        fallback_robot = sorted_robots_by_distance_to_city[0]
        clusters[fallback_robot].append(city)
        remaining_capacity[fallback_robot] -= remaining_demand[city]

# Step 2: Create tours within each cluster (greedy nearest neighbour approach)
def calculate_total_distance(route, include_return_to_depot=True):
    total_distance = 0
    for r in range(1, len(route)):
        total_distance += distances[route[r-1]][route[r]]
    if include_return_to_depot:
        total_distance += distances[route[-1]][0]  # return to depot
    return total_distance

tours = []
total_costs = []

for cluster in clusters:
    if not cluster:
        continue
    tour = [0]  # all tours start at the depot
    current_city = 0  # start at depot
    while cluster:
        # Find the nearest city not yet visited
        next_city = min(cluster, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        current_city = next_city
        cluster.remove(next_city)
    tour.append(0)  # return to depot
    tours.append(tour)
    total_costs.append(calculate_total_distance(tour))

# Outputting final results
overall_total_cost = sum(total_costs)
for i in range(len(tours)):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")