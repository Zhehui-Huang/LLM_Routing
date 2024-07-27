import pulp as pl
import math

# Define city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(city_coordinates)
distance_matrix = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Number of robots and their corresponding depot index
num_robots = 8
depot_indices = list(range(num_robots))

# Sets
depots = set(depot_indices)
cities = set(range(n))
non_depots = cities.difference(depots)

# Variable creation
prob = pl.LpProblem("VRP", pl.LpMinimize)
x = pl.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities for k in depots if i != j), cat='Binary')
u = pl.LpVariable.dicts("u", (i for i in cities if i not in depots), lowBound=0, cat='Continuous')

# Objective function
prob += pl.lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
# Departure from each depot
for k in depots:
    prob += pl.lpSum(x[k, j, k] for j in cities if j != k) == 1, f"Depot_{k}_Departure"

# Each customer node is visited exactly once
for j in non_depots:
    prob += pl.lpSum(x[i, j, k] for i in cities for k in depots if i != j) == 1, f"Visit_{j}"

# Route continuity
for k in depots:
    for i in cities:
        prob += pl.lpSum(x[i, j, k] for j in cities if i != j) == pl.lpSum(x[j, i, k] for j in cities if i != j)

# Subtour elimination
for k in depots:
    for i in non_depots:
        for j in non_depots:
            if i != j:
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] + (n - 3) * x[j, i, k] <= n - 2

# Solve the problem
prob.solve()

# Gather results
tours = {k: [] for k in depots}
for k in depots:
    tour = [k]
    while True:
        next_city = [j for j in cities if j != tour[-1] and pl.value(x[tour[-1], j, k]) == 1]
        if not next_city:
            break
        tour.append(next_city[0])
    tours[k] = tour + [k]

# Display robot tours and costs
overall_cost = 0
for k in depots:
    tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    overall_cost += tour_rate
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {overall_tour_cost}")