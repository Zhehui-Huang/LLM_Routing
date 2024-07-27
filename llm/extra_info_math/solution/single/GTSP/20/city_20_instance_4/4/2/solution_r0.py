from math import sqrt
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Calculate distances between all pairs of cities
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

distances = {(i, j): euclidean calculate distances between all citieseuclidean_distance(i, j) for i in cities for j in cities if i != j}

# Number of groups and a list of all vertices
k = len(groups)
V = range(len(cities))

# Auxilliary variables to represent each group
group_vars = {i: LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(2, k+1)}

# Define the problem
prob = LpProblem("TSP_Groups", LpMinimize)

# x_ij whether edge i->j is part of the solution
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)

# Objective Function
prob += lpSum(x[i, j] * distances[i, j] for i in cities for j in cities if i != j)

# Constraints
# Connect from each group to others
for p_index, group in enumerate(groups, 1):
    prob += lpSum(x[i, j] for i in group for j in V if j not in group) == 1
    prob += lpSum(x[j, i] for i in group for j in V if j not in group) == 1

# Flow conservation
for i in V:
    prob += lpSum(x[j, i] for j in V if j != i) == lpSum(x[i, j] for j in V if j != i)

# Subtour elimination constraints
for p in range(2, k+1):
    for q in range(2, k+1):
        if p != q:
            prob += group_vars[p] - group_vars[q] + k * lpSum(x[i, j] for i in groups[p-1] for j in groups[q-1]) + \
                    (k-2) * lpSum(x[j, i] for i in groups[q-1] for j in groups[p-1]) \
                    <= k - 1

# Solving the problem
prob.solve()

# Retrieve the solution
tour = []
visited = [0]
current = 0

while len(visited) < len(groups) + 1:
    next_city = [j for j in cities if x[current, j].varValue == 1 and j not in visited]
    if next_city:
        next_city = next_city[0]
        tour.append(next_city)
        visited.append(next_city)
        current = next_city
    if current == 0:
        break

tour = [0] + tour + [0]
total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)