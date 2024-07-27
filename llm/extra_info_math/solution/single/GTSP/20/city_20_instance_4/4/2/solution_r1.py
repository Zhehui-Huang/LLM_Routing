from math import sqrt
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Defining city coordinates and groups
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all pairwise distances
distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Variables
selected = [(p, i, j) for p in range(len(groups)) for i in groups[p] for j in cities if i != j]

# Linear Programming Model
model = LpProblem("Minimize_Route_Cost", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (selected), cat=LpBinary)

# Objective function
model += lpSum(x[p, i, j] * distances[i, j] for p, i, j in selected if j in cities)

# Each group should have exactly one exiting edge to a non-group city
for p in range(len(groups)):
    model += lpSum(x[p, i, j] for i in groups[p] for j in cities if j not in groups[p]) == 1

# From each city (except depot), exactly one path chosen
for j in cities:
    if j != 0:
        model += lpSum(x[p, i, j] for p in range(len(groups)) for i in groups[p] if j in cities and i != j) == \
                 lpSum(x[p, j, k] for p in range(len(groups)) for k in cities if k not in groups[p] and k != j)

# Connection back to depot from a city in a group
model += lpSum(x[p, i, 0] for p in range(len(groups)) for i in groups[p]) == 1

# Solve the LP model
model.solve()

# Extract the tour results from variables
tour = [0]
current = 0
while len(tour) <= len(groups):
    next_city = [(i, j) for (p, i, j) in selected if i == current and x[p, i, j].varValue > 0.9]
    if not next_city:
        break
    next_city = next_city[0][1]
    tour.append(next_city)
    current = next_city if next_city != 0 else tour[-1]

tour.append(0)
total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the final tour and cost
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)