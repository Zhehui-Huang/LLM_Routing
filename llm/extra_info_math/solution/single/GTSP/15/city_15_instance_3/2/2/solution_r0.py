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
    14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate all city indices and the cost dictionary
V = list(coordinates.keys())
V_p = groups
k = len(V_p) + 1  # number of clusters including the depot
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in V for j in V if i != j}

# Integer programming setup
prob = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (p for p in range(2, k)), lowBound=0, cat='Continuous')

# Objective Function
prob += pulp.lpSum(c[i, j] * x[i, j] for i in V for j in V if i != j), "Total_Cost"

# Constraints
# Each cluster must be linked exactly once
for group in V_p:
    prob += pulp.lpSum(x[i, j] for i in group for j in V if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in V if j not in group) == 1

# Each city must have one incoming and one outgoing connection
for i in V:
    prob += pulp.lpSum(x[i, j] for j in V if j != i) == 1
    prob += pulp.lpSum(x[j, i] for j in V if j != i) == 1

# Subtour elimination constraints
for p in range(1, k):
    for q in range(1, k):
        if p != q:
            for i in V_p[p-1]:
                for j in V_p[q-1]:
                    prob += u[p] - u[q] + k * x[i, j] + (k - 2) * x[j, i] <= k - 1

# Solve the problem
status = prob.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Extract the solution
tour = []
visited = set()
current_city = 0
while True:
    next_city = next(j for j in V if pulp.value(x[current_city, j]) == 1)
    tour.append(next_city)
    if next_city == 0:
        break
    current_city = next_id

# Calculate total cost
total_cost = sum(c[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")