import math
from itertools import combinations

# Coordinates of cities including the depot
coordinates = [(145, 215), (151, 264), (159, 268), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

# City demands (excluding the depot which is city 0)
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robots details
num_robots = 4
capacity_per_robot = 6000

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix calculation
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke-Wright Savings Algorithm adapted for this problem
# Calculate savings
savings_list = [(i, j, distances[0][i] + distances[0][j] - distances[i][j]) for i in range(1, len(coordinates)) for j in range(i+1, len(coordinates))]
savings_list.sort(key=lambda x: x[2], reverse=True)

# Assign routes to robots
routes = {}
for robot in range(num_robots):
    routes[robot] = [[0]]

current_loads = {robot: 0 for robot in range(num_robots)}

def find_vehicle_for_city(city, demand):
    # Try to fit city into any existing robot routes without exceeding capacity
    for robot, route_groups in routes.items():
        for route in route_groups:
            if current_loads[robot] + demand <= capacity_perarring robot:
                route.append(city)
                current_loads[robot] += demand
                return True
    return False

# Use savings to build feasible routes
for city1, city2, _ in savings_list:
    demand1, demand2 = demands[city1], demands[city2]
    if not find_vehicle_for_city(city1, demand1):
        continue
    if not find_vehicle_for_city(city2, demand2):
        continue

# Calculate the total distance for each robot's tour
total_cost = 0
for robot, route_groups in routes.items():
    for route in route_groups:
        tour_distance = 0
        last_city = 0
        for city in route:
            tour_distance += distances[last_city][city]
            last_city = city
        # Finally, return to the depot
        tour_distance += distances[last_city][0]
        route.append(0)  # End the route with the depot
        print(f"Robot {robot} Tour: {route}")
        print(f"Robot {robot} Total Travel Cost: {tour_distance}")
        total_cost += tour_distance

print(f"Overall Total Travel Cost: {total_cost}")