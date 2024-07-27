import pulp
import math

# City coordinates (including the depot city at index 0)
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

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Problem instance
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# Variables: x[i,j] is 1 if edge from i to j is included in the tour
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(15) for j in range(15) if i != j), cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(15) for j in range(15) if i != j)

# Constraints
# Each group should have exactly one incoming and one outgoing connection with the rest of the tour
for key, group in groups.items():
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(15) if j not in group) == 1
    problem += pulp.lpSum(x[(i, j)] for j in group for i in range(15) if i not in group) == 1

# Flow conservation at each node
for i in range(15):
    problem += pulp.lpSum(x[(i, j)] for j in range(15) if j != i) - pulp.lpSum(x[(j, i)] for j in range(15) if j != i) == 0

# Solve problem
status = problem.solve()

# Tour construction and total travel cost
if status == pulp.LpStatusOptimal:
    tour = [0]
    used_edges = [(i, j) for i in range(15) for j in range(15) if i != j and pulp.value(x[(i, j)]) == 1]
    current_city = 0
    while len(used_edges) > 0:
        for i, j in used_edges:
            if i == current_city:
                tour.append(j)
                current_city = j
                used_edges.remove((i, j))
                break
    tour.append(0)  # Complete the tour by returning to the depot
    
    total_cost = sum(euclidean_manual_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("An optimal solution could not be found.")