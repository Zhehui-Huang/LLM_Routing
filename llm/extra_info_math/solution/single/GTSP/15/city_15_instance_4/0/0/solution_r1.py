import pulp
from math import sqrt

# Defining the coordinates for the depot and cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initiate LP problem
problem = pulp.LpProblem("VRP_Groups", pulp.LpMinimize)

# Decision variables: x_ij where i, j are node indices
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(15) for j in range(15) if i != j), cat='Binary')

# Variables for subtour elimination
u = pulp.LpVariable.dicts("u", (range(2, 15)), lowBound=0, cat='Continuous')

# Objective: Minimize the total distance
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(15) for j in range(15) if i != j)

# Constraints

# Ensure each city is visited exactly once and only one city from each group is part of the tour
for grp in groups:
    problem += pulp.lpSum(x[0][j] for j in grp) == 1
    problem += pulp.lpSum(x[j][0] for j in grp) == 1
    problem += pulp.lpSum(x[i][j] for i in grp for j in range(15) if i != j) == 1
    problem += pulp.lpSum(x[j][i] for i in grp for j in range(15) if i != j) == 1

# Subtour elimination constraints
n = 15
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Solve the problem
problem.solve()

# Extract solution
if pulp.LpStatus[problem.status] == 'Optimal':
    tour = [0]
    current_city = 0
    total_travel_cost = 0
    
    # Create a determined pathway
    while len(tour) < 8:
        next_city = None
        for j in range(15):
            if j != current_city and pulp.value(x[current_city][j]) == 1:
                next_city = j
                break
        tour.append(next_city)
        total_travel_cost += distance(current_city, next_city)
        current_city = next_city
    
    # Complete the tour by returning to the depot
    tour.append(0)
    total_travel_arg += distance(current_city, 0)
    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("No optimal solution found.")