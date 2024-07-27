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
cost = [[0] * n for _ in range(n)]
for i in cities:
    for j in cities:
        if i != j:
            cost[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            cost[i][j] = float('inf')  # Inf cost to prevent self-loop

# Setting up the TSP problem using PuLP
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pulp.LpBinary)

# Objective Function
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    problem += pulp.lpSum(x[i, j] for j in cities if i != j and j in cities) == 1  # Leave each city only once
    problem += pulp.lpSum(x[j, i] for j in cities if i != j and j in cities) == 1  # Arrive each city only once

# Sub-Tour Elimination (preventing solutions that are disjointed loops)
u = pulp.LpVariable.dicts("u", cities, lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n - 2

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the solution
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    total_cost = 0
    for i in cities:
        for j in cities:
            if x[i, j].value() == 1:
                total_cost += cost[i][j]
                tour.append((i, j))

    # Ordering tour based on decisions
    ordered_tour = []
    current_location = 0  # starting point (depot city)
    while len(ordered_tour) < n:
        for (i, j) in tour:
            if i == current_location:
                ordered_tour.append(current_location)
                current_location = j
                break
    ordered_tour.append(0)  # end at the starting city

    print("Tour: ", ordered_tour)
    print("Total travel cost: {:.2f}".format(total_cost))
else:
    print("Failed to find an optimal solution.")