import pulp
import math

# Helper function to compute Euclidean Distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Grouping cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij travel between city i and city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Connect selected cities minimally
for group_id, group in groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in group for j in set(cities.keys()) - set(group)) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in set(cities.keys()) - set(group)) == 1

# Objective function
prob += pulp.lpSum(x[(i, j)] * calc_distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Continuity constraints (subtour elimination constraints might be solved using callback in more advanced solvers like Gurobi/Cplex)
u = pulp.LpVariable.dicts("u", (i for i in cities.keys() if i != 0), lowBound=0, cat='Continuous')

M = len(cities) - 1
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + (M * x[(i, j)]) <= (M-1)

# Solve the problem
prob.solve()

if pulp.LpStatus[prob.status] == 'Optimal':
    print("An optimal solution was found.")
else:
    print("Failed to find optimal solution.")

# Extract result
path = []
visited = [0]
while len(visited) < len(groups) + 1:
    last = visited[-1]
    for k in cities:
        if k not in visited and x[(last, k)].varValue == 1:
            path.append((last, k))
            visited.append(k)
            break
path.append((visited[-1], 0))  # Return to depot

tour = [p[0] for p in path] + [0]
total_cost = sum(calc_completed animation for (i, j) in path)

print("Tour:", tour)
print("Total travel cost:", total_cost)