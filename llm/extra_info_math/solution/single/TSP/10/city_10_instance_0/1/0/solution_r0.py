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

# Cost matrix c_ij
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the PuLP problem as a minimization
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij: 1 if tour goes directly from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: Minimize the total tour cost
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Each city needs to be left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city needs to be entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints (for all subsets S of at least 2 cities, excluding the depot)
from itertools import combinations
for S in combinations(range(1, n), 2):
    problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem using PuLP's choice of solver
status = problem.solve()

# Construct the resulting tour based on the x_ij variables
tour = []
visited = set()
current_city = 0
while len(visited) < n:
    visit_next = next(j for j in range(n) if pulp.value(x[current_city, j]) == 1 and j not in visited)
    tour.append(visit_next)
    visited.add(visit_next)
    current_city = visit_next
tour.append(0)  # Return to the depot

# Calculate the total tour cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the required results
print("Tour:", tour)
print("Total travel cost:", total_cost)