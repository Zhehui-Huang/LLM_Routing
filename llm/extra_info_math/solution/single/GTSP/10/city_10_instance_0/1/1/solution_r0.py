import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# City coordinates (indexed from 0 to 9)
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

# Grouping of cities
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Compute distances
distances = {}
cities = list(coordinates.keys())
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Problem setup
prob = pulp.LpProblem("MinimizeRouteCost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(distances[i, j] * x[i, j] for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
for group in groups.values():
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"One_outgoing_from_group_{group}"
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"One_incoming_to_group_{group}"

for i in cities:
    prob += (pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if j != i)), f"Flow_conservation_{i}"

# Solve the problem
prob.solve()

# Check if a solution exists
if pulp.LpStatus[prob.status] == 'Optimal':
    # Extract the route
    route = []
    visited = [0]  # starting at depot
    while len(visited) < 5:
        current = visited[-1]
        for j in cities:
            if j != current and pulp.value(x[current, j]) == 1:
                visited.append(j)
                break
    visited.append(0)  # end at the depot
    
    # Calculate total travel cost
    total_cost = sum(distances[visited[i], visited[i+1]] for i in range(len(visited) - 1))

    print("Tour:", visited)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")