import math
from itertools import combinations

# Coordinates of cities (including the depot)
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

# Demand for each city
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Distance calculation
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate all distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Number of robots and their capacity
num_robots = 4
capacity_per_robot = 6000

# Util function to calculate the saving between two cities
def savings(city1, city2, depot=0):
    return distances[depot][city1] + distances[depot][city2] - distances[city1][city2]

# Initial individual trips from the depot to each city and back
trips = [[0, i, 0] for i in range(1, len(coordinates))]

# Calculate savings for potential merges and sort them
potential_savings = [(i, j, savings(i, j)) for i, j in combinations(range(1, len(coordinates)), 2)]
potential_savings.sort(key=lambda x: x[2], reverse=True)

# Vehicle assignment preparation
vehicles = [[] for _ in range(num_robots)]
current_capacity = [0] * num_robots

# Apply Clarke-Wright Savings Algorithm with enhancements
for i, j, saving in potential_savings:
    found = False
    for v in vehicles:
        if i in v and j not in v and demands[j] + sum(demands[x] for x in v if x != 0) <= capacity_per_robot:
            v.append(j)
            found = True
            break
        elif j in v and i not in v and demands[i] + sum(demands[x] for x in v if x != 0) <= capacity_per_robot:
            v.append(i)
            found = True
            break
    if not found:
        for v in vehicles:
            if not v:
                if demands[i] + demands[j] <= capacity_per_robot:
                    v.extend([i, j])
                    break

# Solving routing within each vehicle
def plan_route(vehicle):
    route = [0]  # Start at depot
    remaining = set(vehicle)
    while remaining:
        last = route[-1]
        next_city = min(remaining, key=lambda x: distances[last][x])
        route.append(nextcity)
        remaining.remove(nextcity)
    route.append(0)  # Return to depot
    return route

# Plan routes for each vehicle
vehicle_routes = [plan_route(v) for v in vehicles]

# Calculate travel cost for each vehicle's route
vehicle_costs = [sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1)) for route in vehicle_routes]
overall_cost = sum(vehicle_costs)

# Display each vehicle's route and costs
for i, (route, cost) in enumerate(zip(vehicle_routes, vehicle_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")