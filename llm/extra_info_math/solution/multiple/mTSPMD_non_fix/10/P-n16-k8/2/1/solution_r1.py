import math
import pulp

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost matrix
costs = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create a LP problem for the TSP
problem = pulp.LpProblem("Multi_Depot_Multiple_TSP", pulp.LpMinimize)

# Decision variable: x[i, j] = 1 if travel from i to j
x = pulp.LpVariable.dicts("x", (costs), 0, 1, pulp.LpBinary)

# Continuous helper variable for sub-tour prevention
u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), lowBound=1, upBound=len(cities)-1, cat='Continuous')

# Objective Function: Minimize total travel costs
problem += pulp.lpSum([costs[(i, j)] * x[(i, j)] for (i, j) in costs]), "Minimize_Total_Travel_Cost"

# One exit from each depot
for i in range(8):
    problem += pulp.lpSum([x[(i, j)] for j in cities if (i, j) in x]) == 1, f"One_exit_from_depot_{i}"

# One entry to any depot (make optional, robots do not need to return)
for i in range(8):
    problem += pulp.lpSum([x[(j, i)] for j in cities if (j, i) in x]) <= 2, f"One_entry_to_depot_{i}"

# One visit per city excluding depots
for j in cities:
    if j >= 8:  # City is not a depot
        problem += pulp.lpSum([x[(i, j)] for i in cities if (i, j) in x]) == 1, f"One_visit_to_city_{j}"
        problem += pulp.lpSum([x[(j, k)] for k in cities if (j, k) in x]) == 1, f"One_exit_from_city_{j}"

# Subtour Elimination Constraints
n = len(cities)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0 and (i, j) in x:
            problem += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2, f"subtour_elimination_{i}_{j}"

# Solving the Problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Solution status check
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
else:
    print("An optimal solution has not been found.")

# Output solution
overall_cost = 0

for k in range(8):
    tour = [k]
    current_city = k
    cost = 0

    while True:
        next_city = None

        for j in cities:
            if (current_city, j) in x and pulp.value(x[(current_city, j)]) == 1:
                next_city = j
                cost += costs[(current_city, j)]
                tour.append(j)
                break

        if next_city is None or next_city < 8 and len(tour) > 1:
            break

        current_city = next_city

    overall_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")