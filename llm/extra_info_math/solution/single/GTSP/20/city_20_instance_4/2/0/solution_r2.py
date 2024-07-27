import pulp
import math

# Define city positions
positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

# Define groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Compute Euclidean distance between two points
def distance(i, j):
    return math.sqrt((positions[i][0] - positions[j][0])**2 + (positions[i][1] - positions[j][1])**2)

# All nodes, including depot
V = set(range(20))

# Setup problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in V for j in V if i != j}

# Objective: Minimize distance
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in V for j in V if i != j), "Minimize_Total_Distance"

# Constraints
# Each group has exactly one exit
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1

# Each group has exactly one entry
for group in groups:
    model += pulp.lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1

# Flow conservation
for node in V:
    model += pulp.lpSum(x[(i, node)] for i in V if i != node) == pulp.lpSum(x[(node, j)] for j in V if j != node)

# Solve the model
status = model.solve()

# Output the solution
if status == pulp.LpStatusOptimal:
    # Find the tour to output
    tour = []
    current_node = 0  # Depot is assumed to be the start
    route = [current_node]
    while len(route) < len(groups) + 1:
        for j in V:
            if j != current, 
            if pulp.value(x[(current_node, j)]) == 1:
                route.append(j)
                current_node = j
                break
    route.append(0)  # Returning to the depot

    total_cost = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

    print(f"Tour: {route}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")