import pulp
import math

# City coordinates with indices starting at 0 (depot)
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Distance function (Euclidean)
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Variables and problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(len(coordinates)), lowBound=0, cat='Continuous')

# Objective: minimize total travel distance
prob += pulp.lpSum([distance(coordinates[i], coordinates[j]) * x[i, j] for i in coordinates for j in coordinates if i != j])

# Constraints
# Flow maintenance (each city is entered and left exactly once)
for j in coordinates:
    prob += pulp.lpSum([x[i, j] for i in coordinates if i != j]) == 1, f"enter_{j}"
    prob += pulp.lpSum([x[j, i] for i in coordinates if i != j]) == 1, f"leave_{j}"

# Group constraints: one edge in/out per group
for g in groups:
    prob += pulp.lpSum([x[i, j] for i in g for j in coordinates if j not in g]) == 1, f"out_group_{groups.index(g)}"
    prob += pulp.lpSum([x[i, j] for i in coordinates if i not in g for j in g]) == 1, f"in_group_{groups.index(g)}"

# Subtour elimination: Miller-Tucker-Zemlin (MTZ) formulation adapted
K = len(coordinates)
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            prob += u[i] - u[j] + K * x[i, j] <= K - 1

# Solve the problem
prob.solve()

# Extract tour order and calculate cost
tour = [0]
while len(tour) < len(coordinates):
    for j in coordinates:
        if x[tour[-1], j].varValue == 1:
            tour.append(j)
            break

total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)