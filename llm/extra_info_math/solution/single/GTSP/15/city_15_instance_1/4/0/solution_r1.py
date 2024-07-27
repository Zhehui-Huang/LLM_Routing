import pulp
import math

# Define points for depot and 14 other cities
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 64),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Grouping of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Problem setup
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Each group must have exactly one outgoing and one incoming connection
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group and i != j) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group and i != j) == 1

# Flow conservation
for city in cities:
    # Sum of outgoing - incoming edges = 0 for all except depot
    prob += pulp.lpSum(x[city, j] for j in cities if city != j) - pulp.lp.boxSum(x[j, city] for j in cities if city != j) == 0

# The depot must also ensure to only have one incoming and one outgoing edge to/from selected nodes in groups
prob += pulp.lpSum(x[0, j] for j in cities if j != 0 and j in sum(groups, [])) == 1
prob += pulp.lpSum(x[j, 0] for j in cities if j != 0 and j in sum(groups, [])) == 1

# Solve the problem
prob.solve()

# Output tour and total cost
tour = [0]  # start from depot
visited = set([0])
while len(visited) < len(groups) + 1:
    for j in cities:
        if x[tour[-1], j].varValue == 1:
            tour.append(j)
            visited.add(j)
            break
tour.append(0)  # return to depot

# Calculate the total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)