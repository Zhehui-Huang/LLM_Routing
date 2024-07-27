import pulp
from math import sqrt

# Define the city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# City groups:
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize the optimization problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective Function: Minimizing distance
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j), "Total_Distance"

# Flow conservation for groups 
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, "exit_"+str(group)
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, "enter_"+str(group)

# Subtour elimination and flow conservation
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == pulp.lpSum(x[j, i] for j in cities if j != i), f"flow_{i}"

# Resolve and output
model.solve()

# Extract the solution
path = []
visited = set([0])
current_node = 0
while True:
    next_nodes = [j for j in cities if pulp.value(x[current_node, j]) == 1 and j not in visited]
    if not next_nodes:
        # No unvisited nodes - check if it can go back to the depot
        if pulp.value(x[current_node, 0]) == 1:
            path.append(0)
            break
        else:
            print("Error in tour formation.")
            break
    next_node = next_nodes[0]
    path.append(next_node)
    visited.add(next_node)
    current_node = next_node

# Calculate total distance
total_distance = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

# Output results
print(f"Tour: {path}")
print(f"Total travel cost: {total_distance:.2f}")