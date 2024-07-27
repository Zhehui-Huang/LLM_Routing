import pulp
import math

# City coordinates provided in the problem
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Euclidean distance calculator
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Set of nodes and depots
V = set(range(22))
D = {0}  # Only one depot starting for this problem scenario
V_prime = V - D
num_salesmen = 4

# Create the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", V_prime, lowBound=0, cat='Integer')

# Objective function
problem += pulp.lpSum(x[i, j] * euclidean_dist(i, j) for i in V for j in V if i != j)

# Constraints
# 1. Salesmen leave the depot
for i in D:
    problem += pulp.lpSum(x[i, j] for j in V if i != j) == num_salesmen

# 4. Each city is visited exactly once and each salesmen serves at minimum 1 city
for j in V_prime:
    problem += pulp.lpSum(x[i, j] for i in V if i != j) == 1
    problem += pulp.lpSum(x[j, k] for k in V if j != k) == 1

# 5. Subtour elimination
for i in V_prime:
    for j in V_prime:
        if i != j:
            problem += u[i] - u[j] + len(V) * x[i, j] <= len(V) - 1

# Solve the problem
problem.solve()

# Output results
tours = {i: [] for i in D}
for i in V:
    for j in V:
        if i != j and pulp.value(x[i, j]) == 1:
            tours[0].append(j)

# Calculate costs and print outputs
overall_total_cost = 0
print("\n")
for i in D:
    tour = tours[i]
    if tour:
        tour = [0] + tour
        print(f"Robot {i} Tour: {tour}")
        tour_cost = sum(euclidean_dist(tour[k], tour[k+1]) for k in range(len(tour)-1))
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
        overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")