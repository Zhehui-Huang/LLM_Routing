import pulp
import math

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Coordinates for each city, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 45), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
n = len(coordinates)
m = 8  # number of robots

# Problem definition
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective
prob += pulp.lpSum(x[(i, j, k)] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# 1. Each city is visited exactly once by exactly one robot
for j in range(1, n):
    prob += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# 2. Continuity and departure from each city
for k in range(m):
    for i in range(1, n):
        prob += (pulp.lpSum(x[(i, j, k)] for j in range(n) if i != j) - pulp.lpSum(x[(j, i, k)] for j in range(n) if i != j) == 0)

# 3. Departure and Arrival at depot
for k in range(m):
    prob += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# 4. Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# Solve the problem
prob.solve()

# Output results
for k in range(m):
    tour = ['Depot']
    for i in range(n):
        for j in range(n):
            if pulp.value(x[(i, j, k)]) == 1:
                tour.append('City ' + str(j))
                break
    tour.append('Back to Depot')
    tour_cost = sum(euclidean_distance(coordinates[int(tour[i].split()[-1])], coordinates[int(tour[i+1].split()[-1])]) for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")