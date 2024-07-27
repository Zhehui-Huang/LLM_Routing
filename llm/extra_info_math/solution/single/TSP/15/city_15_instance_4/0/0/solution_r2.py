import pulp
import math
import itertools

# Define city coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the cost matrix
cost_matrix = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
               for i in range(n) for j in range(n) if i != j}

# Setup the problem model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# X_ij variables: 1 if path from i to j is taken, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function to minimize total distance
model += pulp.lpSum([cost_matrix[(i, j)] * x[(i, j)] for i in range(n) for j in range(n) if i != j])

# Each city must be entered and left exactly once
for i in range(n):
    model += pulp.lpSum([x[(i, j)] for j in range(n) if (i, j) in x]) == 1  # Leave i
    model += pulp.lpSum([x[(j, i)] for j in range(n) if (j, i) in x]) == 1  # Enter i

# Subtour elimination
for m in range(2, n):
    for S in itertools.combinations(range(n), m):
        model += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j and (i, j) in x) <= len(S) - 1

# Solve the TSP
model.solve(pulp.PULP_CBC_CMD(msg=True))

if model.status == pulp.LpStatusOptimal:
    # Retrieve the optimal tour
    edges_selected = [(i, j) for (i, j) in x if x[(i, j)].varValue == 1]
    
    # Reconstructing the path from list of edges
    current_location = 0
    path = [current_location]
    while len(path) < n:
        next_moves = [j for (i, j) in edges_selected if i == current_location]
        if next_moves:
            current_location = next_moves[0]
            path.append(current_selection)

    # Append start location to complete the cycle
    path.append(path[0])
    total_travel_cost = pulp.value(model.objective)
    
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_travel_route:.2f}")
else:
    print("No feasible solution was found.")