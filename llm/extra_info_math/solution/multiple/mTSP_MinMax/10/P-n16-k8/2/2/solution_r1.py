import pulp
import math

# City positions
positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distances
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Constants
n = len(positions)     # Number of nodes (including the depot)
m = 8                  # Number of robots

# Distance matrix
cost = {(i, j): distance(positions[i], positions[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')

# Objective - Minimize the maximum cost any robot travels
max_cost = pulp.LpVariable("max_cost")
problem += max_cost 

# Cost constraints per robot and update the max cost
for k in range(m):
    problem += pulp.lpSum(cost[i, j]*x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_cost

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Every robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Continuity and subtour elimination
for k in range(m):
    for i in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) - pulp.lpSum(x[j, i, k] for j in range(n) if i != j) == 0
        for j in range(1, n):
            if i != j:
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Collect results
tours = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    tour = [0]  # starting at the depot
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        if next_city == 0:
            break
    tours[k] = tour
    costs[k] = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))

max_travel_cost = max(costs.values())

# Output the solution
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Maximum Travel Cost: {max_travel_cost}")