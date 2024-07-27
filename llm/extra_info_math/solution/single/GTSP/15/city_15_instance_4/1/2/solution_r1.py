import pulp
import math

# Locations for each city
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

# City groups
city_groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}

# Compute Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Prepare the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = {}
u = {}
V = [0] + [c for group in city_groups.values() for c in group]
P = list(range(len(city_groups) + 1))  # including the depot
k = len(P)
for i in V:
    u[i] = pulp.LpVariable(f"u_{i}", lowBound=0, cat=pulp.LpContinuous)
    for j in V:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective function: Minimize the travel cost
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(cities[i], cities[j]) for i in V for j in V if i != j and (i, j) in x), "Minimize_cost"

# Constraints
# Each group must have an exit and entry
for p in range(1, k):  # excluding the depot
    group = city_groups[p - 1]
    problem += pulp.lpSum(x[(i, j)] for i in group for j in V if j not in group and (i, j) in x) == 1, f"exit_group_{p}"
    problem += pulp.lpSum(x[(j, i)] for i in group for j in V if j not in group and (j, i) in x) == 1, f"entry_group_{p}"

# Flow conservation
for i in V:
    problem += pulp.lpSum(x[(j, i)] for j in V if j != i and (j, i) in x) == pulp.lpSum(x[(i, j)] for j in V if j != i and (i, j) in x), f"flow_cons_{i}"

# Subtour elimination
N = len(V)
for i in V:
    if i != 0:  # Exclude depot
        for j in V:
            if i != j and i != 0 and j != 0 and (i, j) in x:
                problem += u[i] - u[j] + N * x[(i, j)] <= N - 1

# Solve the problem
solution_status = problem.solve()

# Check if the solution is optimal
if solution_status == pulp.LpStatusOptimal:
    # Extract the tour
    tour = [0]
    next_city = 0
    while True:
        next_moves = [j for j, var in x.items() if var.value() == 1 and j[0] == next_city]
        if not next_moves:
            break
        next_city = next_moves[0][1]
        tour.append(next_city)
        if next_city == 0:
            break

    total_travel_cost = pulp.value(problem.objective)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
else:
    print("No optimal solution found.")