import pulp
import math
from itertools import combinations

# Coordinates of the cities
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Creating the model
model = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = pulp.LpVariable('max_distance', lowBound=0, cat='Continuous')

# Objective function
model += d, "Maximize leg length"

# Constraints
# Distance constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum_of_outgoing_edges_from_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum_of_incoming_edges_to_{i}"

# Subtour elimination constraints - Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Max distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[i, j] <= d

# Solve the problem
if model.solve() == pulp.LpStatusOptimal:
    print('Model solved successfully!')

    # Construct the tour from the variables
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    current_location = 0
    tour = [current_location]

    while len(edges) > 0:
        for i, j in edges:
            if i == current_location:
                tour.append(j)
                current_location = j
                edges.remove((i, j))
                break

    tour.append(0)  # Returning to the depot

    # Calculate max distance and total cost
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print(f'Tour: {tour}')
    print(f'Total travel cost: {total_cost}')
    print(f'Maximum distance between consecutive cities: {max_distance}')
else:
    print('Failed to solve the model.')