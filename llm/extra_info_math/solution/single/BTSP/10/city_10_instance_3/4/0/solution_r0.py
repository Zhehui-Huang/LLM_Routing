from pulp import *
import math

# Define the cities with their coordinates
cities = {
    0: (84, 67), # depot
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distances between every pair of cities
def distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

# Creating a dictionary to hold the distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Define TSP model
model = LpProblem("TSP_Model", LpMinimize)

# Decision variables: x_ij where i, j represents the cities
x = LpVariable.dicts("x", [(i,j) for i in cities for j in cities if i != j], 0, 1, LpBinary)

# Objective: Minimize the maximum distance between consecutive cities visited
max_distance = LpVariable("Max_Distance")
model += max_distance

# Subject to - exactly one departure from each city
for i in cities:
    model += lpSum(x[(i, j)] for j in cities if i != j) == 1

# Subject to - exactly one arrival at each city
for j in cities:
    model += lpSum(x[(i, j)] for i in cities if i != j) == 1

# Subject to - sub-tour elimination
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):
            model += x[(i,j)] * distances[(i,j)] <= max_distance

# Subtour Elimination Constraints
for S in range(2, len(cities)):
    for subset in combinations(cities.keys(), S):
        if 0 not in subset:  # Include condition to make generation of subsets valid
            model += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Extract tour order
edges = [(i, j) for i in cities for j in cities if i != j and x[(i,j)].varValue == 1]
tour = [0]
while len(edges) > 0:
    for e in edges:
        if e[0] == tour[-1]:
            tour.append(e[1])
            edges.remove(e)
            break

# Close the tour
tour.append(0)

# Calculate the total travel cost
total_cost = sum([distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1)])

# Maximum distance in the optimal tour
max_distance_value = value(max_distance)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_value}")