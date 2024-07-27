import pulp
import math

# Define city coordinates and groups
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance between two points
def calculate_distance(id1, id2):
    return math.sqrt((cities[id1][0] - cities[id2][0]) ** 2 + (cities[id1][1] - cities[id2][1]) ** 2)

# Variables for all pairs i->j except i==j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0) for i in cities}  # for subtour elimination

# Problem definition
prob = pulp.LpProblem("TSP_Grouped_Minimal_Tour", pulp.LpMinimize)

# Objective: Minimize distance
prob += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in cities for j in cities if i != j)

# Constraints for visiting one city from each group
for group in groups.values():
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"Out_{group}"
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"In_{group}"

# Only one entry and one exit for each city
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == pulp.lpSum(x[j, i] for j in cities if i != j), f"Flow_{i}"

# Subtour elimination
n = len(cities)
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0) and i in u and j in u:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
prob.solve()

# Gather the results
tour = [0]
current_city = 0
for _ in range(len(groups) + 1):
    next_city = next(j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1)
    tour.append(next_city)
    current_city = next_city

# Calculate the total cost
total_cost = sum(calculatez_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")