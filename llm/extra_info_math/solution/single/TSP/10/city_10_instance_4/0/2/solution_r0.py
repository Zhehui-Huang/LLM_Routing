import pulp
import math

# Given cities and their coordinates.
cities = {0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
          5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)}

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Formulating the cost matrix
n = len(cities)
cost = [[0]*n for _ in range(n)]
for i in cities:
    for j in cities:
        if i != j:
            cost[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            cost[i][j] = float('inf')  # prevent self-loop

# Create TSP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pulp.LpBinary)

# Objective function: Minimize the sum of travel costs across the tour
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints: Enter and Leave each city exactly once (excluding subtour elimination for now)
for i in cities:
    problem += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # Leave city i exactly once
    problem += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # Enter city i exactly once

# Subtour Elimination Constraints (using MTZ formulation)
u = pulp.LpVariable.dicts("u", cities, lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + (n-1)*x[i, j] <= n-2

# Solving the TSP problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Retrieve results
if status == pulp.LpStatusOptimal:
    tour = []
    total_cost = pulp.value(problem.objective)
    current_city = 0
    tour.append(current_city)
    while len(tour) < n:
        for j in cities:
            if x[current_city, j].varValue == 1:
                current_city = j
                tour.append(current_city)
                break
    tour.append(0)  # return to depot

    print("Tour: " + str(tour))
    print("Total travel cost: " + str(total_cost))
else:
    print("Failed to find an optimal solution")