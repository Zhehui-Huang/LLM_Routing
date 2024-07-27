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

# Objective function: Minimize total distance
solver += pulp.lpSum(x[(i, j)] * euclidean_distance(cities[i], cities[j])
                    for i in cities for j in cities if i != j)

# Constraints: Exact one city per group and connectivity requirements
all_groups = [group_0, group_1, group_2]
all_nodes = [0] + group_0 + group_1 + group_2

# Each group must have exactly one outgoing and incoming link with the rest of the nodes
for group in all_groups:
    solver += pulp.lpSum(x[(i, j)] for i in group for j in all_nodes if j not in group) == 1
    solver += pulp.lpSum(x[(j, i)] for i in group for j in all_nodes if j not in group) == 1

# Flow conservation for each city (excluding depot which is accounted by group constraints)
for v in all_nodes:
    if v != 0:
        solver += pulp.lpSum(x[(v, j)] for j in all_nodes if j != v) \
            == pulp.lpSum(x[(i, v)] for i in all_nodes if i != v)

# Prevent subtours within selected groups
for i in range(1, len(all_nodes)):
    for j in range(1, len(all_nodes)):
        if i != j:
            solver += u[i] - u[j] + len(all_nodes) * x[(i, j)] <= len(all_nodes) - 1

# Solve the ILP problem
if solver.solve() == pulp.LpStatusOptimal:
    total_cost = pulp.value(solver.objective)
    print("Tour optimization successful")
    print("Total travel cost:", total_cost)

    # Displaying the paths that were chosen
    result_tour = []
    for i in all_nodes:
        for j in all_customers:
            if i != j and pulp.value(x[(i, j)]) == 1:
                result_tour.append((i, j))
                print(f"{i} -> {j} with x_{i}_{j} = {pulp.value(x[(i, j)])}")

else:
    print("No optimal solution found.")