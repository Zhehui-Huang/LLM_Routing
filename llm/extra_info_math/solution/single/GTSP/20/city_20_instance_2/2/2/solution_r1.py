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
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# All cities including depot
cities = list(city_locations.keys())

# Distances between each pair of cities (ignoring distances from a city to itself)
distances = {
    (i, j): euclidean_dist(city_locations[i], city_locations[j])
    for i in cities for j in cities if i != j
}

# Create the optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if travel is from city i to city j
x = pulp.LpVariable.dicts(
    "x", ((i, j) for i in cities for j in cities if i != j),
    cat=pulp.LpBinary
)

# Objective: Minimize the total travel distance
model += pulp.lpSum([distances[i, j] * x[i, j] for i, j in distances])

# Constraint: Exactly one connection from each group
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group and i != j) == 1

# Constraint: Exactly one connection to each group
for group in groups:
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group and i != j) == 1

# Constraint: One incoming and one outgoing edge for each city
for city in cities:
    model += pulp.lpSum(x[i, city] for i in cities if i != city) == 1
    model += pulp.lpSum(x[city, j] for j in cities if j != city) == 1

# Solve the problem
status = model.solve()

# Check if the solution is optimal
if status == pulp.LpStatusOptimal:
    tour = [0]
    while len(tour) <= len(groups):
        for j in cities:
            if pulp.value(x[tour[-1], j]) == 1:
                tour.append(j)
                break
    tour.append(0)  # End tour at the depot

    # Calculate the total travel cost
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find an optimal solution. Status:", pulp.LpStatus[status])