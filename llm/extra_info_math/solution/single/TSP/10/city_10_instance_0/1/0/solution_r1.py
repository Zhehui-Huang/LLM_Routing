import pulp
import math

# Coordinates of the cities (including the depot)
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Number of cities (including depot)
n = len(coordinates)

# Calculate the Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create cost matrix c_ij
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n) if i != j]
        if i != j else [] for i in range(n)]

# Prepare the optimization model
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(x[i, j] * cost[i][j] for i in range(n) for j in range(n) if i != j and cost[i])

# Constraints that each city is entered and left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j and j < n and i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j and j < n and i != j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve problem
problem.solve()

# Fetch the tour based on decision variables
tour = [0]
for _ in range(n - 1):
    next_city = next(j for j in range(n) if j not in tour and pulp.value(x[tour[-1], j]) == 1)
    tour.append(next_city)
tour.append(0)  # Append depot city to complete the tour

# Calculate the tour cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print the tour and cost
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))