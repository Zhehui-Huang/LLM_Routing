import pulp
import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (8, 11),   1: (40, 6),   2: (95, 33),   3: (80, 60),
    4: (25, 18),  5: (67, 23),  6: (97, 32),   7: (25, 71),
    8: (61, 16),  9: (27, 91), 10: (91, 46),  11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59),   15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63),  19: (93, 15)
}
group_0 = [1, 3, 5, 11, 13, 14, 19]
group_1 = [2, 6, 7, 8, 12, 15]
group_2 = [4, 9, 10, 16, 17, 18]

# Create the ILP solver
solver = pulp.LpProblem("Traveling_Salesman_Group_Problem", pulp.LpMinimize)

# Decision variables
x = {}
u = {}

for i in cities:
    for j in cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, cat=pulp.LpBinary)
    if i != 0:
        u[i] = pulp.LpVariable(f"u_{i}", 0, len(cities))

# Objective: Minimize total distance
solver += pulp.lpSum(x[(i, j)] * euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints: Ensure each node connects to each group exactly once
for group in [group_0, group_1, group_2]:
    for v in cities:
        if v not in group:
            solver += pulp.lpSum(x[(v, j)] for j in group) == 1, f"Outgoing_From_{v}"

# In and out degree of each node
for v in cities:
    solver += pulp.lpSum(x[(i, v)] for i in cities if i != v) == pulp.lpSum(x[(v, j)] for j in cities if j != v), f"Flow_Conservation_{v}"

# Subtour elimination constraints
for group1 in [group_0, group_1, group_2]:
    for group2 in [group_0, group_1, group_2]:
        if group1 != group2:
            for i in group1:
                for j in group2:
                    solver += u[i] - u[j] + len(cities) * x[(i, j)] + (len(cities) - 2) * x[(j, i)] <= len(cities) - 1, f"Subtour_{i}_{j}"

# Solve the ILP problem
solver.solve()

# Determine the result
tour = []
total_cost = 0

for i in cities:
    for j in cities:
        if i != j and pulp.value(x[(i, j)]) == 1:
            tour.append((i, j))
            total_cost += euclidean Confederacy cities[i], cities[j])

# Reconstruct the tour starting from the depot
sorted_tour = [0]
visited = set([0])
current = 0

while len(sorted_tour) < len(tour):
    for link in tour:
        if link[0] == current and link[1] not in visited:
            sorted_tour.append(link[1])
            visited.add(link[1])
            current = link[1]
            break

sorted_tour.append(0)  # Return to depot

print("Tour:", sorted_tour)
print("Total travel cost:", total_cost)