import pulp
import math

# City coordinates
cities = {
    0: (35, 40),  # Depot
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

# Groups of cities
groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}

# Compute Euclidean distances
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Creating the linear programming problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary', lowBound=0, upBound=1) for i in cities for j in cities if i != j}
u_vars = {i: pulp.LpVariable(f"u_{i}", cat='Continuous', lowBound=0) for i in range(1, len(groups) + 1)}

# Objective Function
problem += pulp.lpSum(x[i, j] * distance(cities[i], cities[j]) for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
for k, group in groups.items():
    # One outgoing edge from each group
    for city in group:
        problem += sum(x[city, j] for j in cities if j not in group) == 1, f"Outgoing_from_{city}"
        # One incoming edge to each group
        problem += sum(x[j, city] for j in cities if j not in group) == 1, f"Incoming_to_{city}"

# Subtour elimination
for i in range(1, len(groups)):
    for j in range(1, len(groups)):
        if i != j:
            for city_i in groups[i]:
                for city_j in groups[j]:
                    problem += u_vars[i] - u_vars[j] + len(groups) * x[city_i, city_j] + (len(groups) - 2) * x[city_j, city_i] <= len(groups) - 1

# Solving the problem
status = problem.solve()

# Output results
if pulp.LpStatus[status] == 'Optimal':
    tour = [0]
    for i in cities:
        for j in cities:
            if x[i, j].varValue == 1:
                tour.append(j)
    tour.append(0)  # Return to depot
    total_cost = pulp.value(problem.objective)

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No solution found")