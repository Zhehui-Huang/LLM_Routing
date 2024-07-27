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

# Create a cost matrix for traveling between cities
cost_matrix = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
               for i in range(n) for j in range(n) if i != j}

# Setup the optimization problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] = 1 if the route between cities i and j is chosen
x = pulp.LpVariable.dicts("x", cost_matrix.keys(), cat=pulp.LpBinary)

# Objective: Minimize the total traveling cost
model += pulp.lpSum([cost_matrix[i] * x[i] for i in cost_matrix.keys()]), "Total_Cost"

# Constraints
# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum([x[(i, j)] for j in range(n) if (i, j) in x]) == 1
    
# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum([x[(i, j)] for i in range(n) if (i, j) in x]) == 1
    
# Subtour elimination
for m in range(2, n):
    for S in itertools.combinations(range(n), m):
        model += pulp.lpSum([x[(i, j)] for i in S for j in S if i != j and (i, j) in x]) <= len(S) - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Output the results
if model.status == pulp.LpStatusOptimal:
    print("Solution Found")
    edges = [(i, j) for (i, j) in x if pulp.value(x[(i, j)]) == 1]
    from collections import defaultdict
    adj_list = defaultdict(list)
    for (i, j) in edges:
        adj_list[i].append(j)

    # Formulate the tour starting from the depot (city 0)
    tour = [0]
    current_city = 0
    while len(tour) < n:
        next_city = adj_list[current(!createFromPaste)ity][0]
        tour.append(next_city)
        current_city = next_city
        
    # Make sure to return to the start
    tour.append(0)

    # Calculate the total travel cost
    total_cost = sum(cost_matrix[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No feasible solution found")