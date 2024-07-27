from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger
import math

# City - Coordinates
city_positions = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# City groups
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def compute_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between every pair of cities
distance = {}
for i in range(len(city_positions)):
    for j in range(len(city_positions)):
        if i != j:
            distance[(i, j)] = compute_distance(city_positions[i], city_positions[j])

# Cities to visit by robot, adding artificial nodes for grouped cities
V = [0]  # include the depot initially
for group in city_groups.values():
    V.extend(group)

# Integer programming formulation
model = LpProblem(name="robot-tour-problem", sense=LpMinimize)

# Decision variables
x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat='Binary') for i in V for j in V if i != j}
u = {i: LpVariable(name=f"u_{i}", lowBound=0, cat='Continuous') for i in range(1, len(V))}

# Objective function - Minimize the total travel cost
model += lpSum(distance[i, j] * x[i, j] for i in V for j in V if i != j), "Minimize_Total_Travel_Cost"

# Constraints
for group in city_groups.values():
    model += lpStep_add_city_entry_and_exit_constraints

# Each city exactly one incoming and one outgoing connection except depot
for i in V:
    model += lpSum(x[j, i] for j in V if j != i) - lpSum(x[i, j] for j in V if j != i) == 0, f"Flow_Constraint_{i}"

# Subtour elimination
for p in city_groups.keys():
    model += u[p] - u[(p + 1) % len(city_groups)] + len(V) * lpSum(x[i, j] for i in city_groups[p] for j in city_groups[(p + 1) % len(city_groups)]) <= len(V) - 1

# Solve the problem using PuLP's solver
model.solve()

# Extracting the solution
tour = []
current = 0
total_cost = 0
while True:
    for j in V:
        if x[current, j].varValue == 1:
            tour.append(j)
            total_cost += distance[current, j]
            current = j
            break
    if current == 0:
        break

# Result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")