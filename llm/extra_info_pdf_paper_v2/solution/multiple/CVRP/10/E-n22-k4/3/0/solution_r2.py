import math

# Definitions
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000
num_robots = 4

# Function to calculate Euclidean distance
def distance(a, b):
    return math.sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

# Initialize tours and loading
tours = [[0] for _ in range(num_robots)]
current_load = [0] * num_robots

# Clarke-Wright Savings Algorithm
savings = []
for i in range(1, len(coords)):
    for j in range(i + 1, len(coords)):
        if demands[i] + demands[j] <= capacity:
            s = distance(0, i) + distance(0, j) - distance(i, j)
            savings.append((s, i, j))

# Sort savings in descending order
savings.sort(reverse=True, key=lambda x: x[0])

# Using a disjoint set to manage the clusters
cluster = list(range(len(coords)))
def find(city):
    if cluster[city] != city:
        cluster[city] = find(cluster[city])
    return cluster[city]

# Apply savings to form clusters with demand constraints
for _, i, j in savings:
    if find(i) != find(j) and current_load[find(i)] + demands[j] <= capacity and currentload[find(j)] + demands[i] <= capacity:
        root_i = find(i)
        root_j = find(j)
        # union
        cluster[root_j] = root_i
        current_load[root_i] += current_load[root_j]
        current_load[root_j] = 0

# Distribute clusters to vehicles
assigned_cities = set()
vehicle_routes = []
for robot in range(num_robots):
    route = [0]
    load = 0
    for city in range(1, len(coords)):
        if find(city) == city and city not in assigned_cities and load + demands[city] <= capacity:
            route.append(city)
            load += demands[city]
            assigned_cities.add(city)
    route.append(0)
    vehicle_routes.append(route)

# Calculate costs
total_cost = 0
for route in vehicle_routes:
    cost = 0
    for i in range(len(route) - 1):
        cost += distance(route[i], route[i + 1])
    print(f"Tour: {route} Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")