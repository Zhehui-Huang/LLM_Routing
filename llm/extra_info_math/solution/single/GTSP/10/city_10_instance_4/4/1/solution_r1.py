import math
from pulp import LpMinimize, LpProblem, LpVariable, LpBinary

# Define cities with their coordinates
cities = {
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
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem
problem = LpProblem("Robot_Tour", LpMinimize)

# Decision Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat=LpBinary) for i in cities for j in cities if i != j}

# Objective: Minimize the distance
problem += lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Ensuring each group has exactly one connection to and from nodes outside the group
for group in groups:
    problem += lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"exit_from_group_{group}"
    problem += lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"enter_to_group_{group}"

# Flow Conservation
for city in cities:
    problem += lpSum(x[(j, city)] for j in cities if (j, city) in x) == lpSum(x[(city, j)] for j in cities if (city, j) in x), f"flow_{city}"

# Prohibit sub-tour formation
u = {i: LpVariable(f"u_{i}", lowBound=0, cat="Continuous") for i in cities if i != 0}
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0 and (i, j) in x:
            problem += u[i] - u[j] + (len(cities) * x[(i, j)]) <= len(cities) - 1

# Solve the problem
problem.solve()

# Extract the solution
tour = [0]
visited = set(tour)
current = 0

while True:
    next_city = None
    for j in cities:
        if j not in visited and x[(current, j)].value() == 1:
            tour.append(j)
            current = j
            visited.add(j)
            next_city = j
            break
    if next_city == 0:
        break

# Total cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the solutions
print("Tour:", tour)
print("Total travel cost:", total_cost)