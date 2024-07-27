import pulp
import math

# Given city coordinates (depot included)
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities including the depot
n = len(cities)

# Create the distance matrix
cost = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Set up the optimization problem: Minimize total travel cost
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] = 1 if travel from i to j, else 0
x = pulp.LpVariable.dicts("x", cost.keys(), cat=pulp.LpBinary)

# Objective function: Minimize total distance
prob += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost.keys()]), "Total_Cost"

# Constraint: Enter and leave each city exactly once
for k in range(n):
    prob += pulp.lpSum([x[i, j] for i, j in x if i == k]) == 1, f"Leave_{k}"
    prob += pulp.lpSum([x[i, j] for i, j in x if j == k]) == 1, f"Enter_{k}"

# Subtour elimination constraints (using MTZ formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
solution_status = prob.solve()
assert pulp.LpStatus[solution_status] == 'Optimal', "An optimal solution was not found!"

# Extract tour starting from the depot
tour = [0]
for _ in range(n-1):
    next_city = next(j for j in range(n) if x[tour[-1], j].varValue == 1)
    tour.append(next_city)

# Closing the loop to return to the depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)