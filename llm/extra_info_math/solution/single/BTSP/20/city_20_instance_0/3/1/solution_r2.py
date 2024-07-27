import pulp
import math
import itertools

# Setup data
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]
n = len(cities)

# Define distance function
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create problem
model = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
d_max = pulp.LpVariable('d_max', lowBound=0, cat='Continuous')

# Objective
model += d_max

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1

for i, j in x.keys():
    model += x[i, j] * distance(cities[i], cities[j]) <= d_max

# Subtour elimination
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[i, j] for i in S for j in S if j != i) <= len(S) - 1

# Solve model
status = model.solve()

if pulp.LpStatus[status] == 'Optimal':
    # Extract solution
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Creating the route as a ordered list of cities
    temp = 0
    route = [temp]
    while len(route) < n:
        for (i, j) in edges:
            if i == temp:
                route.append(j)
                temp = j
                break
    route.append(route[0])  # complete the tour
    
    # Calculate cost and max distance
    total_cost = sum(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
    max_dist = max(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
    
    # Output results
    print(f"Tour: {route}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No optimal solution found.")