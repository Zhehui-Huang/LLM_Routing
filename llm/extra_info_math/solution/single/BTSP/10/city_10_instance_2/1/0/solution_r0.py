import pulp
import math

# Define the coordinates of each city
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate the distance between each pair of cities
n = len(cities)
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = pulp.LpProblem("MinimaxTSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the path from city i to city j is chosen
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Additional variable to capture the maximum distance
max_dist = pulp.LpVariable("max_dist")

# Objective function: Minimize the maximum distance
prob += max_dist

# Constraints:
# Each city is left exactly once
for i in range(n):
    prob += sum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city is entered exactly once
for j in range(n):
    prob += sum(x[(i, j)] for i in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[(i, j)] * x[(i, j)] <= max_dist

# Subtour elimination (via Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the problem
prob.solve()

# Extract the tour from the solution
tour = []
visited = set()
current = 0
for _ in range(n):
    tour.append(current)
    visited.add(current)
    for j in range(n):
        if j not in visited and x[(current, j)].varValue == 1:
            current = j
            break
tour.append(0)

# Calculate the required outputs
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
maximum_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance}")