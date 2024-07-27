from math import sqrt
import pulp

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Problem setup
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(len(coords)) for j in range(len(coords)) if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(1, len(groups) + 1)}

# Objective function
prob += pulp.lpSum(x[i, j] * euclidean_distance(coords[i], coords[j]) for i in range(len(coords)) for j in range(len(coords)) if i != j), "Total_Distance"

# Constraints
## Each group has exactly one outgoing edge to a node outside the cluster
for idx, group in enumerate(groups, start=1):
    prob += sum(x[i, j] for i in group for j in range(len(coords)) if j not in group) == 1, f"One_outgoing_from_group_{idx}"

## Each group has exactly one incoming edge from a node outside the cluster
for idx, group in enumerate(groups, start=1):
    prob += sum(x[j, i] for i in group for j in range(len(coords)) if j not in group) == 1, f"One_incoming_to_group_{idx}"

## Flow conservation constraint
for node in range(len(coords)):
    prob += sum(x[node, j] for j in range(len(coords)) if j != node) == sum(x[j, node] for j in range(len(coords)) if j != node), f"Flow_conservation_at_node_{node}"

# S for u_p - u_q + k*sum(x[i][j]) + (k-2)*sum(x[j][i]) <= k-1 for all p != q

# Solve the problem
if prob.solve() == pulp.LpStatusOptimal:
    optimal_route = [0]
    current_position = 0
    while True:
        found = False
        for j in range(len(coords)):
            if j != current_position and x[(current_position, j)].varValue == 1:
                optimal_route.append(j)
                current_position = j
                found = True
                break
        if not found or current_position == 0:
            break

    optimal_route.append(0)  # Return to the depot
    total_cost = sum(euclidean_distance(coords[optimal_route[i]], coords[optimal_route[i+1]]) for i in range(len(optimal_route) - 1))

    print("Tour:", optimal_route)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found")