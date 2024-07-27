import pulp
import math

# Define the cities and their coordinates
city_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define the groups
groups = {
    0: [0, 4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(2, 7), lowBound=0, upBound=len(groups), cat='Continuous')

# Objective function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(city_coords[i], city_coords[j]) for i in range(20) for j in range(20) if i != j)

# Constraints
# One node per group to outside connection
for p, nodes in groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in nodes for j in range(20) if j not in nodes) == 1
    prob += pulp.lpSum(x[(j, i)] for i in nodes for j in range(20) if j not in nodes) == 1

# Flow conservation
for i in range(20):
    prob += pulp.lpSum(x[(i, j)] for j in range(20) if i != j) == pulp.lpSum(x[(j, i)] for j in range(20) if i != j)

# Subtour elimination
for p, nodes_p in groups.items():
    for q, nodes_q in groups.items():
        if p != q:
            prob += (u[p] - u[q] + len(groups) * pulp.lpSum(x[(i, j)] for i in nodes_p for j in nodes_q) + (len(groups) - 2) * pulp.lpSum(x[(j, i)] for i in nodes_p for j in nodes_q)) <= len(groups) - 1

# Solve the problem
status = prob.solve()

# Output results
tour = [0]
visited = [False]*20
visited[0] = True
current_node = 0
for _ in range(19):
    # Find the next node
    next_node = next(j for j in range(20) if pulp.value(x[(current_node, j)]) == 1 and not visited[j])
    visited[next_node] = True
    tour.append(next_node)
    current_node = next_node
    if next_node == 0:
        break

# Calculate total cost
total_distance = sum(euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_distance)