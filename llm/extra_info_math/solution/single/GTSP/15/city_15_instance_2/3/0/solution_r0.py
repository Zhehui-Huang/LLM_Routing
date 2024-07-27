import pulp
import math

# City coordinates {city_index: (x, y)}
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities (1-based index to 0-based index adjustment in the dictionary)
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Calculate Euclidean Distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Variables
V = [0] + [city for sublist in groups.values() for city in sublist]  # all nodes

# Pulp model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat=pulp.LpBinary)

# Objective Function
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in V for j in V if i != j)

# Each cluster must have exactly one outgoing edge to a node outside the cluster
for group_idx, group in groups.items():
    model += pulp.lpSum(x[(i, j)] for i in group for j in set(V)-set(group)) == 1
    
# Each cluster must have exactly one incoming edge from a node outside the cluster
for group_idx, group in groups.items():
    model += pulp.lpSum(x[(j, i)] for i in group for j in set(V)-set(group)) == 1

# Flow conservation constraint
for k in V:
    model += pulp.lpSum(x[(j, k)] for j in V if j != k) == pulp.lpSum(x[(k, i)] for i in V if i != k)

# Solve model
model.solve()

# Extract tour
tour = []
used_edges = [(i, j) for i in V for j in V if i != j and pulp.value(x[(i, j)]) == 1]
current_node = 0
while len(used_edges) > 0:
    for edge in used_edges:
        if edge[0] == current_node:
            tour.append(current_node)
            current_node = edge[1]
            used_edges.remove(edge)
            break

tour.append(0)  # returning to the depot

# Total travel cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")