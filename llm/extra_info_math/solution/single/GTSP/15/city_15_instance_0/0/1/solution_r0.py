import pulp
import math

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# All cities including the depot
V = list(cities.keys())

# Compute distances matrix
distances = {}
for i in V:
    for j in V:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Optimization problem
prob = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), 
                          cat='Binary')

# Objective
prob += pulp.lpSum(distances[i, j] * x[i, j] for i in V for j in V if i != j)

# One outgoing for each city group
for group in city_groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in V if j not in group) == 1

# One incoming for each city group
for group in city_groups:
    prob += pulp.lpSum(x[j, i] for i in group for j in V if j not in group) == 1

# Flow conservation
for i in V:
    prob += pulp.lpSum(x[j, i] for j in V if j != i) == pulp.lpSum(x[i, j] for j in V if j != i)

# Subtour elimination
u = pulp.LpVariable.dicts("u", (i for i in V if i != 0), lowBound=0, cat='Continuous')
k = len(V) - 1 # number of cities visited in the tour
for i in V:
    if i != 0:
        for j in V:
            if j != 0 and i != j:
                prob += u[i] - u[j] + (k * x[i, j]) <= k - 1

# Solve the problem
prob.solve()

# Extract tour
tour = []
for i in V:
    for j in V:
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Simplify tour to a readable format
sorted_tour = [0]  # Start at depot
visited = set([0])
while len(sorted_tour) < k + 1:
    for i, j in tour:
        if i == sorted_tour[-1] and j not in visited:
            sorted_tour.append(j)
            visited.add(j)
            break
sorted_tour.append(0)  # End at depot

# Calculate total cost
total_cost = sum(distances[sorted_tour[i], sorted_tour[i+1]] for i in range(len(sorted_tour) - 1))

print("Tour:", sorted_tout)
print("Total travel cost:", total_cost)