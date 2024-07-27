import math
from itertools import combinations

# City coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
]

# Parameters
num_robots = 4
robot_capacity = 6000

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Initialize savings list
savings = []
for i, j in combinations(range(1, len(cities)), 2):
    cost_ij = euclidean_distance(i, j)
    cost_0i = euclidean_distance(0, i)
    cost_0j = euclidean_distance(0, j)
    savings.append((i, j, cost_0i + cost_0j - cost_ij))

# Sort savings by savings value in descending order
savings.sort(key=lambda x: x[2], reverse=True)

# Clarke-Wright algorithm to form initial routes
routes = []
used = set()
for i, j, saving in savings:
    if i not in used and j not in used and demands[i] + demands[j] <= robot_capacity:
        routes.append([0, i, j, 0])
        used.update([i, j])

# Attempt to add remaining cities to existing routes
for i in range(1, len(cities)):
    if i not in used:
        for route in routes:
            if sum(demands[c] for c in route if c != 0) + demands[i] <= robot_capacity:
                pos = next(p for p in range(1, len(route)) if euclidean_distance(route[p-1], i) + euclidean_distance(i, route[p]) < euclidean_distance(route[p-1], route[p]) )
                route.insert(pos, i)
                used.add(i)
                break

# Distribute remaining routes among robots
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
for route in routes:
    idx = current_loads.index(min(current_loads))
    tours[idx].extend(route)
    current_loads[idx] += sum(demands[c] for c in route if c != 0)

# Calculate the total travel cost
def calculate_route_cost(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))

total_cost = 0
for i, tour in enumerate(tours):
    cost = calculate_route_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")