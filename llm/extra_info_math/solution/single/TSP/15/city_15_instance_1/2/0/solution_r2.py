import pulp
import math
import itertools

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)

# Create the problem variable to contain the problem data
tsp_problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective function
tsp_problem += pulp.lpSum(x[i, j] * calc_distance(coordinates[i], coordinates[j])
                           for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    tsp_problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    tsp_problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
# Using the Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            tsp_problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
tow_solver = pulp.getSolver('PULP_CBC_CMD')
tsp_problem.solve(tow_solver)

# Retrieving the solution tour
tour = []
if pulp.LpStatus[tsp_problem.status] == 'Optimal':
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    # Construct the tour by following edges from 0
    next_city = 0
    while True:
        next_edge = [e for e in edges if e[0] == next_city][0]
        tour.append(next_city)
        next_city = next_edge[1]
        if next_city == 0:
            break
    tour.append(0)  # Append the start city to complete the tour

    # Calculate the total travel cost
    total_cost = sum(calc_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Output the results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Optimal solution not found.")