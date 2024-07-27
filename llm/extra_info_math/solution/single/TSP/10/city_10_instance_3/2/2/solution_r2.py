import pulp
from math import sqrt
import itertools

# Coordinates of cities (depot + cities 1 to 9)
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Total cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the cost matrix
cost_matrix = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

# PuLP model setup
model = pulp.LpProblem("Traveling_Salesman", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Each city has exactly one incoming and one outgoing connection
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination using Miller-Tucker-Zemlin (MTZ) formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Constraint to avoid self-loops (implicitly satisfied by the binary condition but added for clarity)
for i in range(n):
    x[i, i] = 0

# Solve the problem
model.solve()

# Extract the tour from the solution
tour = []
current = 0
while True:
    tour.append(current)
    next_cities = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if next_cities == []:
        break
    current = next_cities[0]
tour.append(0)  # Ensure tour ends back at the depot

# Calculate the cost of the tour
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")