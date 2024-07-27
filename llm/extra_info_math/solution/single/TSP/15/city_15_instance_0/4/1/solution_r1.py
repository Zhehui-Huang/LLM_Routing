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

# Calculate the distance matrix
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

n = len(cities)
cost = {(i, j): calculate_distance(i, j) for i in range(n) for j in range(n) if i != j}

# Create the LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum([cost[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j]), "Total Travel Cost"

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"Leave_from_{i}"
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"Enter_to_{i}"

# Subtour Elimination Constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the problem
prob.solve()

# Extract the tour
tour = []
visited = [0]
current = 0
while len(visited) < n:
    next_city = next(j for j in range(n) if j != current and x[current,j].varValue == 1)
    tour.append(next_city)
    visited.append(next_city)
    current = next_city

# Complete the tour by returning to the depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")