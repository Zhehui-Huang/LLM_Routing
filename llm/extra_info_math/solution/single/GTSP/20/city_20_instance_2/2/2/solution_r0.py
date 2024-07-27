import pulp
import math
from itertools import product

# Define the city locations and city groups
city_locations = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Total cities including depot
cities = list(city_locations.keys())

# Calculate distances between each pair of cities
distances = {(i, j): euclidean_dist(city_locations[i], city_locations[j]) for i, j in product(cities, cities) if i != j}

# Create the optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if travel is from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pulp.LpBinary)

# Objective: Minimize the total travel distance
model += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Constraints
# One outgoing connection from each group
for g in groups:
    model += pulp.lpSum([x[i, j] for i in g for j in set(cities) - set(g) if i != j]) == 1

# One incoming connection to each group
for g in groups:
    model += pulp.lpSum([x[j, i] for i in g for j in set(cities) - set(g) if i != j]) == 1

# Connectivity constraints to make sure there is only one tour covering all nodes including the depot
for city in cities:
    model += pulp.lpSum(x[city, j] for j in cities if j != city) == 1
    model += pulp.lpSum(x[j, city] for j in cities if j != city) == 1

# Solve the problem
model.solve()

# Extract tour results
tour = []
visited = [0]  # start from the depot city
while len(visited) < len(groups) + 1:
    for j in cities:
        if x[visited[-1], j].varValue == 1:
            visited.append(j)
            break
tour = visited + [0]  # return to the depot

# Calculate the total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)