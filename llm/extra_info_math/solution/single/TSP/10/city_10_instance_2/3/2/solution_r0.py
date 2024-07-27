import pulp
from math import sqrt

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
    (i, j): euclidean_distance(cities[i], cities[j])
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

# Subtour elimination
for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        prob += pulp.lpSum([x[i, j] for i in subset for j in subset if i != j and (i, j) in x]) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current = 0
while True:
    tour.append(current)
    next_cities = [j for j in cities if (current, j) in x and pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    current = next_cities[0]

tour.append(0)  # Return to the depot
total_cost = pulp.value(prob.objective)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)