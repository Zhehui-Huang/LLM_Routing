import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between points
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Constants and Variables
n = len(cities)
m = 2

x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-2, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    # Start from the depot
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    # Ensure the salesman returns to the depot
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - \
                   pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

for i in range(2, n):
    for j in range(2, n):
        for k in range(m):
            if i != j:
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
problem.solve()

# Output results
for k in range(m):
    tour_k = [0]
    while len(tour_k) <= sum([1 for v in x.values() if pulp.value(v) == 1 and v.name.endswith(f"_{k}")]):
        next_city = [j for i in tour_k for j in range(n) if pulp.value(x[tuple(sorted([i,j])+[k])]) == 1 and j not in tour_k]
        tour_k.extend(next_city)
    tour_k.append(0)  # Return to depot

    # Tour cost
    tour_cost = sum(distance(tour_k[i], tour_k[i+1]) for i in range(len(tour_k)-1))
    print(f"Robot {k} Tour: {tour_k}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

# Calculating overall total cost
overall_total_cost = sum(distance(tour_k[i], tour_k[i+1]) for k in range(m) for i in range(len(tour_k)-1))
print(f"Overall Total Travel Cost: {overall colspan=2:2f}")