import pulp
import math

# City coordinates with indices starting at 0 (depot)
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Distance function (Euclidean distance)
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Pulp problem initialization
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j],
                          cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(distance(coordinates[i], coordinates[j]) * x[(i, j)]
                   for i in coordinates for j in coordinates if i != j)

# Constraints
# Ensure only one outgoing connection from each group selection
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in coordinates if j not in group) == 1

# Ensure only one incoming connection to each group selection
for group in groups:
    prob += pulp.lpSum(x[(j, i)] for i in group for j in coordinates if j not in group) == 1

# Ensure continuity and return to depot
for j in coordinates:
    if j != 0:
        prob += pulp.lpSum(x[(i, j)] for i in coordinates if i != j) == 1
        prob += pulp.lpSum(x[(j, k)] for k in coordinates if k != j)== 1

# Solve the problem
prob.solve()

# Extracting the route from the decision variables
tour = []
current_location = 0
while True:
    next_location = [j for j in coordinates if pulp.value(x[(current_location, j)]) == 1][0]
    tour.append(next_location)
    current_location = next_location
    if current_location == 0:
        break

# Calculating total cost
total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)