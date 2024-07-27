import pulp
import math

# Define the cities with coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups are defined as lists of city indices
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Prepare distance matrix
distances = {(i, j): euclidean_lift(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the optimization problem
prob = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Variables x[i, j]: 1 if the path from city i to city j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function to minimize total distance
prob += pulp.lpSum(x[i, j] * distances[i, j] for i in cities for j in cities if i != j)

# Each group has exactly one city visited
for group in city_va:
    prob += pulp.lpSum(x[0, i] for i in group) == 1  # One outgoing connection from depot
    prob += pulp.lpSum(x[i, 0] for i in group) == 1  # One incoming connection to depot

# Ensuring the flow conservation for other grouping conditions
for k, group in enumerate(city_gbc):
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1  # Outgoing from group
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1  # Incoming to group

# Execution of problem
prob.solve()

# Result extraction
tour = [0]
cost = 0
while len(tour) < len(city_groups) + 1:
    for i in cities:
        if i != tour[-1] and pulp.value(x[tour[-1], i]) == 1:
            tour.append(i)
            cost += distances[tour[-2], i]
            break
tour.append(0)  # Back to depot
cost += distances[tour[-2], 0]

print("Tour:", tour)
print("Total travel cost:", cost)