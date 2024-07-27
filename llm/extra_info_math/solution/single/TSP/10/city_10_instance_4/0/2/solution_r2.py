import pulp
import math

# Define the cities coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculating Euclidean distance between points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Formulating the cost matrix
n = len(cities)
cost = [[0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setup the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(cost[i][j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for k in range(n):
    problem += pulp.lpSum(x[(i, k)] for i in range(n) if i != k) == 1  # Arrive
    problem += pulp.lpSum(x[(k, j)] for j in range(n) if k != j) == 1  # Depart

# Sub-tour elimination (MTZ)
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1)*x[(i, j)] <= n-2

# Solve the problem
problem.solve()

# Get the tour
tour = []
for i in range(n):
    for j in range(n):
        if i != j and x[(i, j)].varValue == 1:
            tour.append((i, j))

# Order the tour
ordered_tour = [0]
while len(ordered_tour) < n:
    last = ordered_tour[-1]
    next_city = [j for (i, j) in tour if i == last][0]
    ordered_tour.append(next_city)

ordered_tour.append(0)  # return to the depot

# Calculate total distance
total_distance = sum(cost[i][j] for i, j in zip(ordered_tour[:-1], ordered_tour[1:]))

# Output results
print("Tour: ", ordered_tour)
print("Total travel cost: {:.2f}".format(total_distance))