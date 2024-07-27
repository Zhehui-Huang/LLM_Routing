import numpy as np
import cvxpy as cp
import math

# Coordinates including depots
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
n = len(city_coordinates)
depots = [0, 1]
robots_per_depot = [1, 1] # Each depot dispatches 1 robot

# Euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Variables and problem setup
x = cp.Variable((n, n), boolean=True)
u = cp.Variable(n, integer=True)

# Objective
objective = cp.Minimize(cp.sum(cp.multiply(distances, x)))

# Constraints
constraints = []

# Depart from each depot exactly robots_per_depot times
for depot, count in zip(depots, robots_per_depot):
    constraints.append(cp.sum(x[depot, :]) == count)

# Each non-depot city is visited exactly once
for j in range(n):
    if j not in depots:
        constraints.append(cp.sum(x[:, j]) == 1)
        constraints.append(cp.sum(x[j, :]) == 1)

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j:
            constraints.append(u[i] - u[j] + n * x[i, j] <= n - 1)

# Solve the problem
problem = cp.Problem(objective, constraints)
result = problem.solve(solver=cp.GUROBI, verbose=True)

# Checking x to see values
print(f"x values post-solve (rounded): {np.round(x.value)}")

def retrieve_tour(start_city):
    visited = np.zeros(n, dtype=bool)
    tour = []
    current_city = start_city

    while True:
        tour.append(current_city)
        visited[current_city] = True
        next_cities = np.where(x.value[current_city, :] >= 0.5)[0]
        if len(next_cities) == 0:
            break
        current_city = next_cities[0]
        if visited[current_city]:
            break

    return tour

# Calculate tours and costs
tours = []
tour_costs = []

for depot in depots:
    tour = retrieve_tour(depot)
    tours.append(tour)
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    tour_costs.append(tour_cost)

# Output results
overall_cost = sum(tour_costs)
print(f"Overall Total Travel Cost: {overall_cost}")
for i, tour in enumerate(tours):
    print(f"Robot {i+1} (Depot {depots[i]}) Tour: {tour}")
    print(f"Robot {i+1} Total Travel Cost: {tour_costs[i]}")