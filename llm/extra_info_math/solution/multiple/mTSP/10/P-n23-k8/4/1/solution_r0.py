import pulp
import math
from itertools import product

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates (depot + cities)
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

num_cities = len(coords)
num_robots = 8
depot_city = 0

# Distance matrix
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)]
             for i in range(num_cities)]

# Problem initialization
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, upBound=num_cities-1, cat='Continuous')

# Objective
prob += pulp.lpSum(distances[i][j] * x[i][j][k] for i, j, k in product(range(num_cities), range(num_cities), range(num_robots)))

# Constraint 1: Each city is visited exactly once by one robot
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i][j][k] for i in range(num_cities)
                       for k in range(num_robots)) == 1
    
# Constraint 2: Flow conservation
for k in range(num_robots):
    for p in range(1, num_cities):
        prob += pulp.lpSum(x[p][j][k] for j in range(num_cities)) - \
                pulp.lpSum(x[i][p][k] for i in range(num_cities)) == 0

# Constraint 3: Each robot leaves the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[depot_city][j][k] for j in range(1, num_cities)) == 1

# Constraint 4: Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += u[i] - u[j] + (num_cities-1) * x[i][j][k] <= num_cities - 2

# Solving the problem
prob.solve()

# Extracting solutions
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    tours[k] = [depot_city]
    next_city = depot_city
    while True:
        next_city = next(j for j in range(num_cities) if pulp.value(x[next_city][j][k]) == 1)
        if next_city == depot_city:
            tours[k].append(next_city)
            break
        tours[k].append(next_city)

# Calculate and display the tour costs and overall cost
overall_cost = 0
for k in range(num_robots):
    tour_cost = sum(distances[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")