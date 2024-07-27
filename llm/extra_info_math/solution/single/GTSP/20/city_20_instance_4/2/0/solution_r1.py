import pulp
import math

positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
    (64, 72), (14, 89)
]

groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate Euclidean distances
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Set of all nodes including the depot city
V = list(range(20))

model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j
x = {
    (i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
    for i in V for j in V if i != j
}

# Objective function
model += pulp.lpSum(x[(i, j)] * distance(positions[i], positions[j]) for i in V for j in V if i != j), "Total Distance"

# Constraint: ensure exactly one departure from each group
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1

# Constraint: ensure exactly one arrival in each group
for group in groups:
    model += pulp.lpSum(x[(i, j)] for j in group for i in V if i not in group) == 1

# Flow conservation at each node
for k in V:
    model += pulp.lpSum(x[(i, k)] for i in V if i != k) == pulp.lpSum(x[(k, j)] for j in V if j != k)

# Solve the problem
model.solve()

# Output the result if it's optimal
if model.status == pulp.LpStatusOptimal:
    chosen_edges = [(i, j) for i in V for j in V if i != j and pulp.value(x[(i, j)]) == 1]
    # Recover tour from chosen edges
    tour = []
    current_node = 0
    tour.append(current_node)
    while len(tour) <= len(groups):
        for i, j in chosen_edges:
            if i == current_node:
                tour.append(j)
                current_node = j
                break
    tour.append(0)  # Go back to the depot
    total_cost = sum(distance(positions[i], positions[j]) for i, j in zip(tour[:-1], tour[1:]))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")