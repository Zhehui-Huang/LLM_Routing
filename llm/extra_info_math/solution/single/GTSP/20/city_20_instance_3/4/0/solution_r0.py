import pulp
import math

# Coordinates of all cities including depot city 0
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Euclidean distance calculation
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Variables
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(x[i, j] * dist(i, j) for i in cities for j in cities if i != j)

# Constraints
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group and i != j) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group and i != j) == 1

model += pulp.lpSum(x[j, i] - x[i, j] for i in cities for j in cities if i != j) == 0

# Define the subtour variable u to prevent subtours
u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), lowBound=0, upBound=len(cities)-1, cat='Continuous')

# Subtour elimination constraints
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + len(cities)*x[i, j] <= len(cities)-1

# Solve
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    total_cost = pulp.value(model.objective)
    path = [0]
    current_city = 0
    while len(path) < 7:
        next_city = next(j for j in cities if x[current_city, j].value() == 1)
        path.append(next_city)
        current_city = next_city
    path.append(0)  # return to the depot

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost:.2f}")

else:
    print("Optimal solution not found.")