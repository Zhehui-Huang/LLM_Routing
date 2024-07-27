import pulp
import math

# City coordinates as provided, including the depot (index 0)
cities = [
    (9, 93),
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Groups as provided
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create problem instance
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# Set of all vertexes
V = set(range(15)) 
# Subset of groups including depot
V_p = [0] + sum(groups.values(), [])

# Decision variables x_ij are 1 if path from i to j is chosen, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in V for j in V if i != j)

# Constraints

# Each group should have exactly one incoming and one outgoing edge
for group in groups.values():
    problem += pulp.lpSum(x[(i, j)] for i in V for j in group if i != j) == 1
    problem += pulp.lpSum(x[(i, j)] for j in V for i in group if i != j) == 1

# Flow conservation at nodes
for k in V:
    problem += pulp.lpSum(x[(i, k)] for i in V if i != k) == pulp.lpSum(x[(k, j)] for j in V if j != k)

# Solve problem
status = problem.solve()

# Tour reconstruction and total cost evaluation
tour = [0]
current_city = 0
while len(tour) < 5:  # 1 visit per group + initial city
    for j in V:
        if x[(current_city, j)].varValue == 1:
            tour.append(j)
            current_city = j
            break
tour.append(0)  # returning to depot

# Calculate total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))