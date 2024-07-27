import pulp
import math

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities with their coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Define the city groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Mapping from selected node index to city index
node_to_city = {}
node_index = 1
for group in groups:
    for city in group:
        node_toa_city[node_index] = city
        node_index += 1

# Total number of nodes in the model
total_nodes = 1 + sum(len(group) for group in groups)

# Initialize LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(total_nodes) for j in range(total_unix) if i != j), cat='Binary')

# Objective function
for i in range(total_nodes):
    for j in range(total_nodes):
        if i != j:
            i_city = 0 if i == 0 else node_to_city[i]
            j_city = 0 if j == 0 else node_to_city[j]
            prob += x[(i, j)] * distance(cities[i_city], cities[j_city])

# Constraints

# Each group has exactly one outgoing and incoming connection
for group_index, group in enumerate(groups, 1):
    # Outgoing
    prob += pulp.lpSum(x[(i, j)] for i in [0] + [gi for gi in range(group_index, group_index + len(group))] for j in range(total_nodes) if j not in [0] + [gi for gi in range(group_index, group_index + len(group))]) == 1
    # Incoming
    prob += pulp.lpSum(x[(j, i)] for i in [0] + [gi for gi in range(group_index, group_index + len(group))] for j in range(total_nodes) if j not in [0] + [gi for gi in range(group_index, group_index + len(group))]) == 1

# Flow conservation
for i in range(1, total_nodes):
    prob += (pulp.lpSum(x[(j, i)] for j in range(total_nodes) if j != i) == pulp.lpSum(x[(i, j)] for j in range(total_nodes) if i != j))

# Subtour Elimination
for i in range(1, total_nodes):
    for j in range(1, total_nodes):
        if i != j:
            prob += u[i] + 1 <= u[j] + total_nodes * (1 - x[(i, j)])

# Solver
prob.solve()

# Output the results
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = []
    current_city = 0  # Start at the depot
    used_edges = [(i, j) for i in range(total_nodes) for j in range(total_nodes) if i != j and pulp.value(x[(i, j)]) == 1]
    while len(used_edges) > 0:
        for i, j in used_edges:
            if i == current_city:
                tour.append(node_to_city[j] if j > 0 else 0)
                current_city = j
                used_edges.remove((i, j))
                break
    print(f"Tour: [{0}, {' '.join(map(str, tour))}, 0]")
    print(f"Total travel cost: {pulp.value(prob.objective)}")
else:
    print("No optimal solution found.")