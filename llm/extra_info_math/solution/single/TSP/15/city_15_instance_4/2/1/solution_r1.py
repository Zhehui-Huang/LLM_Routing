import pulp
import math
import itertools

# Define the cities' coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

# Compute costs between every pair of cities
n = len(cities)
cost = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost[(i, j)] = euclidean_distance(cities[i], cities[j])
        else:
            cost[(i, j)] = float('inf')  # Avoid self-loop

# Setting up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
for j in range(n):
    prob += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination
for s in range(2, n):
    for subtour in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i][j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))  # Including msg=0 to suppress solver output

# Extract the solution
tour = [0]
next_city = 0
while True:
    for j in range(n):
        if pulp.value(x[next_city][j]) == 1:
            next_city = j
            break
    if next_city == 0:
        break
    tour.append(next_city)

tour.append(0)  # Close the tour

# Total distance calculation
total_distance = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_distance)