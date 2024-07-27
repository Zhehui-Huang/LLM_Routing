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

# Constants
n = len(cities)
m = 2

x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for i in range(n):
        problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) == pulp.lpSum(x[j, i, k] for j in range(n) if i != j)

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Output results
total_cost = 0
for k in range(m):
    tour = [0]
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                tour.append(j)

    # Close the tour
    tour.append(0)

    # Calculate the cost of the tour
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    total_cost += tour_cost

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")