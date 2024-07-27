import pulp
import math

# Coordinates of each city including the depot city 0
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate the Euclidean distance between pairs of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
cost = {(i, j): calculate_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function: minimize the sum of distances
model += pulp.lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + x[i][j] * n <= n - 1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current_city][j]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

# Calculate total cost of the tour
tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1)) + cost[tour[-1], tour[0]]  # To return to the depot

# Output result
print("Tour:", tour + [tour[0]])
print("Total travel cost:", tour_cost)