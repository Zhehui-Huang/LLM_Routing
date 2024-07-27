import math
import pulp

# City coordinates
coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79),
}

# City groups
groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9],
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Problem setup
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(15) for j in range(15) if i != j}

# Objective function
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in range(15) for j in range(15) if i != j)

# Constraints for visiting exactly one city from each group
for group in groups.values():
    prob += pulp.lpSum(x[0, j] for j in group) == 1
    prob += pulp.lpSum(x[j, 0] for j in group) == 1

# Subtour constraints
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(1, 15)}
k = len(groups) + 1

for i in range(15):
    for j in range(1, 15):
        if i != j:
            prob += u[i] - u[j] + (k * x[i, j]) <= k - 1

# Capacity constraints: ensure each city is connected properly
for j in range(1, 15):
    prob += pulp.lpSum(x[i, j] for i in range(15) if i != j) == pulp.lpSum(x[j, i] for i in range(15) if i != j)

# Solve the problem
prob.solve()

# Output the results
tour = [0]
visited = {0}
current_city = 0
total_cost = 0

if pulp.LpStatus[prob.status] == 'Optimal':
    while len(visited) < len(coordinates):
        for j in range(15):
            if pulp.value(x[current_city, j]) == 1:
                tour.append(j)
                total_cost += distance(current_city, j)
                current_city = j
                visited.add(j)
                break
    total_cost += distance(current_city, 0)  # Return to depot
    tour.append(0)  # Complete the tour by returning to the depot

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No solution found")