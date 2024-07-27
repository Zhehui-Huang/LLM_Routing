import numpy as amdarray
import pulp

# Define the city coordinates and groups
city_coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
                    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
                    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
                    (51, 58), (30, 48)]
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Calculate Euclidean distances
def euclidean_distance(i, j):
    xi, yi = city_coordinates[i]
    xj, yj = city_coordinates[j]
    return np.sqrt((xi - xj)**2 + (yi - yj)**2)

# Number of the groups
k = len(groups)
V = [0] + [city for group in groups for city in group]  # Expanded list of cities including depot
n = len(V)

# Create the problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the path from i to j is used, 0 otherwise
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in V for j in V if i != j}

# Objective: Minimize total travel distance
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in V for j in V if i != j), "TotalTravelCost"

# Constraints to select exactly one node from each group
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in V if i != j) == 1  # exactly one edge out of each group
    problem += pulp.lpSum(x[(j, i)] for j in group for i in V if i != j) == 1  # exactly one edge into each group

# Flow conservation at each city
for i in V:
    problem += pulp.lpSum(x[(i, j)] for j in V if i != j) - pulp.lpSum(x[(j, i)] for j in V if j != i) == 0

# Subtour elimination using additional variables
u = {i: pulp.LpVariable(f"u_{i}", lowBound=1, upBound=(n-1), cat='Continuous') for i in V if i != 0}
for i in V:
    if i != 0:
        for j in V:
            if j != 0:
                problem += (u[i] - u[j] + (n - 1) * x[(i, j)]) <= (n - 2)

# Solve the linear programming problem
problem.solve()

# Retrieve solution
tour = []
active_edges = [(i, j) for i in V for j in V if i != j and pulp.value(x[(i, j)]) == 1]
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for i, j in active_edges if i == current_city]
    if not next_cities:
        break
    current_city = next_cities[0]

# Estimating total cost
total_cost = sum(euclidean_distance(i, j) for i, j in zip(tour[:-1], tour[1:]))

# Output results
print(f"Tour: {tour + [0]}")  # including the return to the depot
print(f"Total travel cost: {total_cost:.2f}")