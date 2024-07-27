import pulp
import math
import itertools

# Define the coordinates of the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(coordinates)  # Number of cities

# Function to calculate Euclidean distance
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance matrix
dist = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective
prob += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for m in range(2, n):
    for S in itertools.combinations(range(n), m):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = prob.solve()

# Retrieve solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Construct the order of the tour
order = []
current_location = 0
for _ in range(n):
    next_location = [j for i, j in tour if i == current_location][0]
    order.append(current_location)
    current_location = next_location
order.append(0)  # to return to the starting point

# Calculate the cost of the tour
tour_cost = sum(dist[order[i]][order[i+1]] for i in range(len(order)-1))

# Produce final outputs
print("Tour:", order)
print("Total travel cost:", round(tour_cost, 2))