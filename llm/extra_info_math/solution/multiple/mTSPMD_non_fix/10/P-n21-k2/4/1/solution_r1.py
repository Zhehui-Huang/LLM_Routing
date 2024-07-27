import pulp
from math import sqrt
import itertools

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of salesmen and depots
depots = [0]
n_robots = 2

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize pulp LP model
model = pulp.LpProblem("MultiDepotTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(21) for j in range(21) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(21), lowBound=0, upBound=21, cat=pulp.LpInteger)

# Objective function
model += pulp.lpSum([euclidean_distance(coordinates[i], coordinates[j]) * x[(i, j)] for i, j in x]), "Sum of Travel Costs"

# Constraints
# Each customer node is visited exactly once
for j in range(21):
    model += (pulp.lpSum([x[(i, j)] for i in range(21) if i != j]) == 1, f"Enter_{j}")
    model += (pulp.lpSum([x[(j, k)] for k in range(21) if j != k]) == 1, f"Leave_{j}")

# Subtour prevention constraints
N = len(coordinates)
for i in range(1, N):
    for j in range(1, N):
        if i != j:
            model += u[i] - u[j] + N * x[(i, j)] <= N - 1

# Solve the model
model.solve()

# Extracting solution
routes = {}
for i in depots:
    route = []
    current = i
    while True:
        next_town = [j for j in range(21) if pulp.value(x[(current, j)]) == 1]
        if not next_town:
            break
        next_town = next_town[0]
        route.append(next_town)
        current = next_town
        if next_town in depots:
            break
    routes[i] = route

# Calculating and printing routes and costs
total_travel_cost = 0
for start_depot, path in routes.items():
    print(f"Robot {start_depot} Tour: {[start_depot] + path}")
    if path:
        cost = sum(euclidean_distance(coordinates[path[i]], coordinates[path[(i+1) % len(path)]]) for i in range(len(path)-1))
        print(f"Robot {start_depot} Total Travel Cost: {cost}")
        total_travel_cost += cost
    else:
        print(f"Robot {start_depot} Total Travel Cost: 0")

print(f"Overall Total Travel Cost: {total_travel_cost}")