import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Grouping cities
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate distances
distances = {}
for i in coordinates:
    for j in coordinates:
        if i != j:
            distances[(i, j)] = euclidean_with_rounding(coordinates[i], coordinates[j])

# Integer programming formulation
prob = pulp.LpProblem("MinimizeRouteCost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in coordinates for j in coordinates if i != j), cat='Binary')

# Objective
prob += pulp.lpSum(distances[i, j] * x[i, j] for i in coordinates for j in coordinates if i != j), "TotalCost"

# Ensure that exactly one node from each group connects to another group
for group_id, group in groups.items():
    # Nodes in group to all nodes not in group (outgoing)
    prob += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group) == 1, f"exit_group_{group_id}"

    # All nodes not in group to nodes in group (incoming)
    prob += pulp.lpSum(x[j, i] for i in group for j in coordinates if j not in group) == 1, f"enter_group_{group_id}"

# Flow conservation
for k in coordinates:
    prob += (pulp.lpSum(x[i, k] for i in coordinates if i != k) ==
             pulp.lpSum(x[k, j] for j in coordinates if j != k)), f"flow_{k}"

# Solve the problem
prob.solve()

# Check solution status
if pulp.LpStatus[prob.status] == 'Optimal':
    print("Optimal Solution Found!")
    # Get the optimal tour
    tour = [0]
    while len(tour) < 5:
        next_city = [j for j in coordinates if j != tour[-1] and pulp.value(x[tour[-1], j]) == 1]
        if not next_city:
            break
        tour.append(next_city[0])
    tour.append(0)  # Return to the depot

    # Total travel cost
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution available.")