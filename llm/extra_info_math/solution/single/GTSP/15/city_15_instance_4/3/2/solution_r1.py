import pulp as pl
import math

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities excluding the depot
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Flatten grouped cities and include the depot as a virtual node
cities = [0] + [city for group in groups for city in group]

# Create problem instance
problem = pl.LpProblem("Minimize_Tour_Cost", pl.LpMinimize)

# Compute distances dictionary
distances = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Variables
x = pl.LpVariable.dicts("edge", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective: Minimize the total travel cost
problem += pl.lpSum([distances[i, j] * x[i, j] for i, j in distances]), "TotalTravelCost"

# Adding constraints
# Each city needs exactly one incoming and one outgoing edge
for k in cities:
    problem += pl.lpSum([x[i, k] for i in cities if i != k]) == 1, f"Incoming_to_{k}"
    problem += pl.lpSum([x[k, j] for j in cities if j != k]) == 1, f"Outgoing_from_{k}"

# Subtour elimination constraints
u = pl.LpVariable.dicts("u", (i for i in cities if i != 0), lowBound=0, upBound=len(cities)-1, cat='Continuous')
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Select one city from each group
for group in groups:
    problem += pl.lpSum([x[(i, j)] for i in group for j in cities if i != j]) == 1
    problem += pl.lpSum([x[(j, i)] for i in group for j in cities if i != j]) == 1

# Solve the LP
problem.solve()

# Finding the tour
current = 0
tour = [current]
# Tracking the number of possible steps to prevent infinite loops
steps = 0

while len(tour) < len(cities) + 1:
    steps += 1
    if steps > 100:  # Safeguard against infinite loops
        break

    next_city = next(j for j in cities if j != current and x[(current, j)].varValue == 1)
    tour.append(next_city)
    current = next_city
    if current == 0:
        break  # Once return to depot, break the loop

# Total Travel Cost
total_cost = pl.value(problem.objective)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)