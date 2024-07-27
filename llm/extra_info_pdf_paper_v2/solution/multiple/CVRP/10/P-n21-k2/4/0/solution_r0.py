import math
from heapq import heappush, heappop

# Define cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Define demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6,
           19, 11, 12, 26, 17, 6, 15]

# Params for robots
robot_capacity = 160
num_robots = 2

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their coordinates. """
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 +
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Calculate initial distances between each city and the depot
distance_to_depot = {i: euclidean_distance(0, i) for i in range(1, len(coordinates))}

# Compute savings: Sij = di0 + d0j - dij for i != j
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        if i != j:
            saving = (euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_data i, j))
            savings.append((saving, i, j))
# Sort savings in descending order (highest savings first)
savings.sort(reverse=True, key=lambda x: x[0])

# Clarke-Wright algorithm to determine initial routes
def clarke_wright():
    routes = []
    load = {}
    for (_, i, j) in savings:
        if demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            load[len(routes)-1] = demands[i] + demands[j]
    return routes, load

# Enhanced CW improvements (Simplified version)
def enhance_routes(routes, load):
    # Placeholder for two-phase probabilistic and route post-improvement procedures
    return routes  # For simplicity in this demo, returning unchanged routes

def assign_and_optimize_routes():
    global routes, load
    routes, load = clarke_wright()
    routes = enhance_routes(routes, load)
    
    total_cost = 0
    detailed_cost = []
    print("Routing Information:")
    for index, route in enumerate(routes):
        cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))
        detailed_cost.append((route[:], cost))
        total_cost += cost
        print(f"Robot {index} Tour: {route}")
        print(f"Robot {index} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

assign_and_optimize_routes()