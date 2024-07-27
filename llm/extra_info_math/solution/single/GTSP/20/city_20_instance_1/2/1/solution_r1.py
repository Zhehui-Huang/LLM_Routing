import pulp
import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

num_groups = len(groups)

# Calculating distances
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Problem
prob = pulp.LpProblem("VRP_Selective_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", list(cities.keys()), lowBound=0, cat='Continuous')

# Objective
prob += pulp.lpSum([distances[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j]), "Total Cost"

# Constraints
# Cluster visitation constraints
for g, members in groups.items():
    prob += pulp.lpSum([x[(i, j)] for i in members for j in cities if j not in members]) == 1, f"Out_cluster_{g}"
    prob += pulp.lpSum([x[(j, i)] for i in members for j in cities if j not in members]) == 1, f"In_cluster_{g}"

# Flow conservation constraints
for k in cities:
    prob += (pulp.lpSum([x[(i, k)] for i in cities if i != k]) ==
             pulp.lpSum([x[(k, j)] for j in cities if j != k])), f"Flow_{k}"

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):
            prob += u[i] - u[j] + (len(cities) * x[(i, j)]) <= len(cities)-1

# Solve problem
prob.solve()

# Extract the solution
tour = [0]
current = 0
for _ in range(len(groups) + 1):
    next_city = [j for j in cities if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city

# Since starting point is 0 and also the ending, we verify if correctly ends at 0
if tour[-1] != 0:
    tour.append(0)

# Calculate the cost
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)