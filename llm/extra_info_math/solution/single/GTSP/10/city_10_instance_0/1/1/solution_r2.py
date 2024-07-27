import pulp
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

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

groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j}

prob = pulp.LpProblem("MinimizeRouteCost", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(2, 4)), lowBound=0, cat='Continuous')

# Objective Function
prob += pulp.lpSum(distances[i, j] * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints
for g, nodes in groups.items():
    # Outgoing
    prob += pulp.lpSum(x[i, j] for i in nodes for j in coordinates if j not in nodes) == 1
    # Incoming
    prob += pulp.lpSum(x[j, i] for i in nodes for j in coordinates if j not in nodes) == 1

# Flow Conservation
for k in coordinates:
    prob += pulp.lpSum(x[i, k] for i in coordinates if (i, k) in x) == pulp.lpSum(x[k, j] for j in coordinates if (k, j) in x)

# Subtour elimination constraints
group_keys_list = list(groups.keys())
K = len(group_keys_list)
for p in range(1, K):
    for q in range(p + 1, K):
        gp = groups[group_keys_list[p]]
        gq = groups[group_keys_list[q]]
        prob += (u[p + 1] - u[q + 1] + (K + (K-2)) * sum(x[i][j] for i in gp for j in gq if (i, j) in x)) <= K - 1

# Solve problem
prob.solve()

# Extract routes and calculate the cost
if pulp.LpStatus[prob.status] == "Optimal":
    active_edges = [(i, j) for i in coordinates for j in coordinates if (i, j) in x and pulp.value(x[i, j]) == 1]
    tour = [0]
    while len(active_edges) > 0:
        for i, j in active_edges:
            if i == tour[-1]:
                tour.append(j)
                active_edges.remove((i, j))
                break
    total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("Optimal solution not found.")