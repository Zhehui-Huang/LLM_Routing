import pulp
import math

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Helper function to calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of cities including the depot
n = len(cities)

# Create a problem instance
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective
prob += z, "Minimize the longest distance between consecutive cities"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"One outboud from {i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"One inbound to {i}"

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * calc_distance(i, j) <= z, f"Max distance constraint for {i}->{j}"

# Subtour prevention constraints
for s in range(3, n+1):
    for S in itertools.combinations(range(1, n), s-1):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
visited = {0}
current = 0
while len(visited) < n:
    for j in range(n):
        if x[current, j].value() == 1:
            tour.append(j)
            visited.add(j)
            current = j
            break

tour = [0] + tour + [0]

# Calculate total travel cost
total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Calculate maximum distance
max_distance = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)