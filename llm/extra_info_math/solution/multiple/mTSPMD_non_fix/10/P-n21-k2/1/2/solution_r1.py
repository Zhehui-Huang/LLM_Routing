import pulp
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

num_vehicles = 2
depots = range(num_vehicles)  # Assume the first num_vehicles cities are depots

n = len(cities)

# Creating distance matrix
distances = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat="Binary")

# Objective function
prob += pulp.lpSum([x[i, j] * distances[i, j] for i in range(n) for j in range(n) if i != j]), "Total_Cost"

# Constraints
# Exactly one exit and one entry per city
for j in range(n):
    if j not in depots:
        prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
        prob += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1

# Vehicle leaves depot only once and returns only once
for i in depots:
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=(n-1), cat="Continuous")
for i in range(n):
    for j in range(n):
        if i != j and i not in depots and j not in depots:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Output solution
routes = {i: [] for i in depots}
costs = {}

for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            routes[i if i in depots else None].append(j)

# Calculating and printing results
overall_total_cost = 0
for depot in depots:
    tour = [depot]
    while routes[depot]:
        next_city = routes[depot].pop(0)
        tour.append(next_city)
        routes[depot] = [x for x in routes[next_city] if x not in tour]
    tour.append(depot)
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    overall_total_cost += tour
    
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")