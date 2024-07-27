import pulp
import math

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

# Function to calculate Euclidean distance
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

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij where i, j are distinct
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city should be left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1

# Each city should be entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1

# Subtour elimination constraints
for subtour_size in range(2, n):
    for subset in itertools.combinations(range(1, n), subtour_size):
        prob += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract solution
tour = []
visited = {0}
current = 0
while len(visited) < n:
    for j in range(n):
        if x[current][j].varValue == 1:
            tour.append(current)
            current = j
            visited.add(current)
            break

tour.append(0)  # return to start point

# Calculate the total travel cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)