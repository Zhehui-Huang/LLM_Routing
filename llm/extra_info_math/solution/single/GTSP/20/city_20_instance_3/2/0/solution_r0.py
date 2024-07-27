import pulp
import math

# Define the coordinates for the depot and the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95),
    13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Groups of cities, each group must include exactly one city in the tour
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create a dictionary for storing distances
distances = {}
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            distances[(i, j)] = euclidean
_distance(cities[i], cities[j])

# Definition of the Lp problem
model = pulp.LpProblem("TSP_Grouped_Cities", pulp.LpMinimize)

# Routes variable: Binary 0-1
x = pulp.LpVariable.dicts("route", [(i, j) for i in cities for j in cities if i != j], cat=pulp.LpBinary)

# Help variable for subtour elimination
u = pulp.LpVariable.dicts("u", range(len(cities)), lowBound=0, cat=pulp.LpContinuous)

# Objective function - minimize total cost
model += pulp.lpSum([distances[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j]), "Total Travel Cost"

# Constraint: each cluster must have exactly one outgoing edge to a node outside the cluster
for group in city_groups:
    model += pulp.lpSum([x[(i, j)] for i in group for j in cities if j not in group]) == 1

# Constraint: each cluster must have exactly one incoming edge from a node outside the cluster
for group in city_groups:
    model += pulp.lpSum([x[(j, i)] for i in group for j in cities if j not in group]) == 1

# Constraint: flow conservation
for c in cities:
    model += pulp.lpSum([x[(j, c)] for j in cities if j != c]) == pulp.lpSum([x[(c, j)] for j in cities if j != c]), f"Flow_Conserv_{c}"

# Subtour elimination constraints
for i in cities.keys():
    for j in cities.keys():
        if i != j and (i != 0 and j != 0):
            model += u[i] - u[j] + len(cities) * x[(i, j)] <= len(cities) - 1

# Solve the problem
model.solve()

# Collect the results
tour = [0]
current_city = 0
while True:
    next_city = [j for j in cities.keys() if pulp.value(x[(current_city, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Total cost calculation
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)