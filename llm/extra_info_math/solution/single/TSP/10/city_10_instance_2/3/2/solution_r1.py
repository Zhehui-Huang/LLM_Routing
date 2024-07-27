import pulp
from math import sqrt
import itertools

# Define distances
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Number of cities
n = len(cities)

# Distance matrix
distances = {
    (i, j): euclideanerer(p1;e(distance(cities[i], cities[j]))
    for i in cities for j in cities if i != j
}

# Create the problem variable:
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 
                          cat='Binary', lowBound=0, upBound=1)

# Objective
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j]), "Total Travel Cost"

# Constraints
for c in cities:
    # Exactly one outgoing edge from each node
    prob += pulp.lpSum([x[i, j] for i in cities if (i, j) in x for j in cities if i != j and j == c]) == 1
    # Exactly one incoming edge to each node
    prob += pulp.lpSum([x[i, j] for j in cities if (i, j) in x for i in cities if i != j and i == c]) == 1

# Subtour elimination constraints
for size in range(2, n + 1):
    for subset in itertools.combinations(cities, size):
        if 0 not in subset: continue  # ignore subsets that do not include the depot
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if (i, j) in x and i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
current = 0
nodes_left = list(cities.keys())
nodes_left.remove(0)
while nodes_left:
    next_moves = [j for j in nodes_left if pulp.value(x[current, j]) == 1]
    if next_moves:
        next_city = next_moves[0]
        tour.append(next_city)
        nodes_left.remove(next_city)
        current = next_city

# Closing the tour by returning to the depot
tour.append(0) 

# Calculate the total tour cost
total_cost = pulp.value(prob.objective)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)