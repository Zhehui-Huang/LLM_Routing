import pulp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Parameters
n = len(cities)  # Number of nodes including depot
m = 8  # Number of robots

# Distance matrix
c = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the optimization problem
prob = pulp.LpProblem("Multiple_TSP_Multisalesman_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), cat='Binary')  # travel selections
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')  # position in tour

# Objective
prob += pulp.lpSum(c[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Each robot starts and ends at the depot, visits the cities
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i][j][k] for i in range(n)) - pulp.lpSum(x[j][i][k] for i in range(n)) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i][j][k] <= n - 2

# Solve the problem
prob.solve()

# Output results
overall_cost = 0
for k in range(m):
    print(f"Robot {k} Tour: ", end="")
    tour = []
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tour.append(j)
    print([0] + tour)
    tour_cost = sum(c[tour[i - 1]][tour[i]] for i in range(1, len(tour)))
    overall_cost += tour_cost
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")