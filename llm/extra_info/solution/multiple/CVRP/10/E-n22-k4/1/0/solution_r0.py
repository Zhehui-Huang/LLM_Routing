import math
from itertools import combinations

# City coordinates (indexed by city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800,
           100, 500, 600, 1200, 1300, 1300, 300, 900,
           2100, 1000, 900, 2500, 1800, 700]

NUM_ROBOTS = 4
CAPACITY = 6000
depot = 0

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Precompute distances
distances = {}
for c1, c2 in combinations(range(len(coordinates)), 2):
    dist = distance(c1, c2)
    distances[(c1, c2)] = dist
    distances[(c2, c1)] = dist
for i in range(len(coordinates)):
    distances[(i, i)] = 0

# Assign cities to robots roughly respecting the capacity constraint
assigned_cities = [[] for _ in range(NUM_ROBOTS)]
remaining_capacity = [CAPACITY] * NUM_ROBOTS
for city, demand in enumerate(demands):
    if city == depot:
        continue
    # Assign city to the robot with the most remaining capacity that can still fit the demand
    possible_robots = [(remaining_capacity[i], i) for i in range(NUM_ROBOTS) if remaining_capacity[i] >= demand]
    if possible_robots:
        _, robot_id = max(possible_robots)
        assigned_cities[robot_id].append(city)
        remaining_capacity[robot_id] -= demand

# Nearest Neighbor algorithm to find route for each robot starting from the depot
def find_route(cities):
    route = [depot]
    unvisited = set(cities)
    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda x: distances[(last, x)])
        route.append(next_city)
        unvisited.remove(next_city)
    route.append(depot)
    return route

# Compute routes and costs
total_cost = 0
for robot_id in range(NUM_ROBOTS):
    tour = find_route(assigned_cities[robot_id])
    tour_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robotid_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")