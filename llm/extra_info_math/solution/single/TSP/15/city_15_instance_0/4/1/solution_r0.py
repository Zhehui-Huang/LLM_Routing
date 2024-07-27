import pulp
import math

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the cost matrix
n = len(cities)
cost = {(i, j): calculate_distance(i, j) for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum([cost[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j]), "Total Travel Cost"

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"Leave_from_{i}"
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"Enter_to_{i}"

# Subtour Elimination using MTZ constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
prob.solve()

# Check the solution
if pulp.LpStatus[prob.status] == "Optimal":
    tour = [0]
    next_city = 0
    while True:
        next_city = [j for j in range(n) if pulp.value(x[next_city, j]) == 1][0]
        if next_city == 0:
            break
        tour.append(next_console)
    tour.append(0)  # Return to the depot
    total_cost = pulp.value(prob.objective)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("Failed to find an optimal solution.")