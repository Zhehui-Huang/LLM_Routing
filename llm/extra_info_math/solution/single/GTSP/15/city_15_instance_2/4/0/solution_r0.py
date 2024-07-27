import pulp
import math

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Distance calculation (Euclidean)
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Establish the model
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities.keys() for j in cities.keys() if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(2, len(groups) + 2), lowBound=0, cat='Continuous')

# Objective
model += pulp.lpSum(distance(i, j) * x[i, j] for i in cities.keys() for j in cities.keys() if i != j)

# Constraints
# Each group must connect to one node outside the group exactly once 
for p, group in enumerate(groups, 1):
    model += pulp.lpSum(x[i, j] for i in group for j in cities.keys() if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities.keys() if j not in group) == 1

# Flow conservation
for i in cities.keys():
    model += (pulp.lpSum(x[j, i] for j in cities.keys() if j != i) 
            - pulp.lpSum(x[i, j] for j in cities.keys() if j != i)) == 0

# Subtour elimination constraints
k = len(groups) + 1 # Including depot group as essentially a group
for p in range(2, k):
    for q in range(2, k):
        if p != q:
            model += u[p] - u[q] + k * pulp.lpSum(x[i, j] for i in groups[p-2] for j in groups[q-2]) + (k-2) * pulp.lpSum(x[j, i] for i in groups[p-2] for j in groups[q-2]) <= k-1

# Solve model
status = model.solve()

# Extract solution
tour = []
visited = {0}
current = 0
while len(visited) < len(groups)+1:
    for j in cities.keys():
        if pulp.value(x[current, j]) == 1:
            tour.append(j)
            visited.add(j)
            current = j
            break
tour = [0] + tour

# Calculate total cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)