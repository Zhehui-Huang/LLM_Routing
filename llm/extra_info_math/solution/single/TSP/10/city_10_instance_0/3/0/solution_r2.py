import math
from pulp import LpMinimize, LpProblem, LpVariable, LpBinary, lpSum

# Define city coordinates including the depot
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(p1, p2):
    return math.dist(p1, p2)

n = len(coordinates)
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the LP problem
model = LpProblem("TSP", LpMinimize)

# Variables
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)]

# Objective: minimize the total travel cost
model += lpSum(cost[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leaving city i
    model += lpSum(x[j][i] for j in range(n) if i != j) == 1  # Entering city i

# Subtour elimination constraints
for s in range(2, n):
    for subset in combinations(range(1, n), s):
        model += lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Retrieve the tour order and total travel cost for output
tour = [0]
current = 0
while True:
    next_city = None
    for j in range(n):
        if x[current][j].value() == 1.0 and j != current:
            next_city = j
            break
    if next_city == 0:
        tour.append(0)
        break
    else:
        tour.append(next_city)
        current = next_city

total_travel_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost))