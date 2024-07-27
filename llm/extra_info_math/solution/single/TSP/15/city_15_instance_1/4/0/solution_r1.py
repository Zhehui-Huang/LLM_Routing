import math
from itertools import combinations
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value

# Define distance calculation function
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# City coordinates
coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Number of cities including depot
n = len(coordinates)

# Cost matrix
cost = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = [[LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective function
prob += lpSum(cost[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Leaving and entering each city constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):
        prob += lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the tour from the variables
tour = []
current_city = 0
while True:
    next_city = None
    for j in range(n):
        if x[current_city][j].value() == 1:
            tour.append(current_city)
            current_city = j
            break
    if current_city == 0:
        break

tour.append(0)  # close the tour at the depot city

# Calculate the tour cost
tour_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel fou", tour_cost)