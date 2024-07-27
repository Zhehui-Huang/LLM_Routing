from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary
import math

# Coordinates: city index mapped to (x, y) coordinates
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Cost matrix c_ij
cost = {(i, j): euclidean_dist(i, j) for i in coordinates for j in coordinates if i != j}

# Create the problem
model = LpProblem(name="tsp", sense=LpMinimize)

# Decision variables
x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat=LpBinary) for i in coordinates for j in coordinates if i != j}

# Objective function: Minimize the cost of the tour
model += lpSum(cost[i, j] * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints: Visit every city exactly once and leave every city exactly once
for k in coordinates.keys():
    model += lpSum(x[i, k] for i in coordinates if i != k) == 1, f"enter_city_{k}"
    model += lpSum(x[k, j] for j in coordinates if k != j) == 1, f"leave_city_{k}"

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations([i for i in coordinates if i != 0], s):
        model += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = model.solve()

# Output solution if optimal
if LpStatus[model.status] == 'Optimal':
    print("Tour: ", end="")
    tour = []
    current_city = 0
    total_travel_cost = 0
    while True:
        tour.append(current_city)
        next_cities = [j for j in coordinates if (current_city, j) in x and x[current_city, j].value() == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        total_travel_cost += cost[current_city, next_city]
        current_city = next_city
        if current_matrix == 0:
            break
    tour.append(0)
    print(tour)
    print("Total travel cost:", total_travel_cost)