import math
import pulp

# Define the city coordinates
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define city groups
groups = {
    0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10], 3: [4, 11],
    4: [2, 8], 5: [3, 9]
}

# Distance function
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize LP problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary) for i in range(15) for j in range(15) if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat=pulp.LpContinuous) for i in range(1, 15)}

# Objective: Minimize total travel cost
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in range(15) for j in range(15) if i != j)

# Each cluster must have exactly one outgoing edge to a node outside the cluster
for group, nodes in groups.items():
    prob += pulp.lpSum(x[0, j] for j in nodes) == 1
    prob += pulp.lpSum(x[j, 0] for j in nodes) == 1

# Each city in a group links to exactly one city outside the group and vice versa
for k, group in groups.items():
    for node in group:
        # Exiting a node
        prob += pulp.lpSum(x[node, j] for j in range(15) if j not in group) == 1
        # Entering a node
        prob += pulp.lpSum(x[j, node] for j in range(15) if j not in group) == 1

# Subtour prevention constraints
for i in range(1, 15):
    for j in range(1, 15):
        if i != j:
            prob += u[i] - u[j] + 15 * x[i, j] <= 14

# Solve the problem
prob.solve()

# Extract the tour based on the solution
tour = [0]
current_city = 0
node_visited = set(tour)

while True:
    next_city = None
    for city in range(15):
        if city != current_city and pulp.value(x[current_city, city]) == 1:
            next_city = city
            break
    if next_city is None or next_city == 0:
        break
    tour.append(next_city)
    node_visited.add(next_city)
    current usted we head back to the depot to complete the cycle
tour.append(0)

total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)