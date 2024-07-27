import numpy as np
from scipy.spatial.distance import pdist, squareform
from mip import Model, xsum, minimize, BINARY

# City Indices and Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Distance matrix
coords = np.array(coordinates)
dist_matrix = squarefrom(pdist(coords, 'euclidean'))

# Model
model = Model()

V = list(range(len(coordinates)))  # all nodes
D = list(range(num_robots))  # depots
V_prime = list(set(V) - set(D))  # non-depot nodes

# Decision variables
x = [[[model.add_var(var_type=BINARY) for k in D] for j in V] for i in V]
u = [model.add_var() for i in V]

# Objective Function: minimize the sum of the travel distances
model.objective = minimize(xsum(dist_matrix[i][j] * x[i][j][k]
                                 for i in V for j in V for k in D))

# Constraints
# Salesmen depart from each depot
for k in D:
    model += xsum(x[k][j][k] for j in V_prime) == 1

# Each customer node is visited exactly once by any depot
for j in V_prime:
    model += xsum(x[i][j][k] for i in V for k in D) == 1

# Subtour elimination
for k in D:
    for i in V:
        model += xsum(x[i][j][k] for j in V) == xsum(x[j][i][k] for j in V)
    for i in V_prime:
        for j in V_prime:
            if i != j:
                model += u[i] - u[j] + len(V) * x[i][j][k] <= len(V) - 1

# Solve the model
model.optimize()

# Extract the robot tours from the variables
tours = {k: [] for k in D}
for k in D:
    tour = [k]
    for _ in range(len(V)):
        next_city = [j for j in V if model.vars[x[tour[-1]][j][k].index].x == 1]
        if not next_city:
            break
        tour.extend(next_city)
    tours[k] = tour

# Calculate costs for each tour and overall
tour_costs = []
total_cost = 0
for k in D:
    tour_cost = sum(dist_matrix[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    tour_costs.append(tour_cost)
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print("Overall Total Travel Cost:", total_cost)