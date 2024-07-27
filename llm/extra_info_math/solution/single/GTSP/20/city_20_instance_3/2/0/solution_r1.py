import pulp
import math

# Define the coordinates for the depot and the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95),
    13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Define the model
model = pulp.LpProblem("TSP_Grouped_Cities", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(len(cities)), 0, None, pulp.LpContinuous)

# Objective
model += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Constraints
for group in city_groups:
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

for c in cities:
    model += pulp.lpSum([x[j, c] for j in cities if j != c]) == pulp.lpSum([x[c, j] for j in cities if j != c])

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Solve the model
status = model.solve()

# Retrieve the solution
tour = []
if status == pulp.LpStatusOptimal:
    current_city = 0
    tour.append(current_city)
    visited = set()
    while True:
        visited.add(current_city)
        next_cities = [j for j in cities if pulp.value(x[(current_city, j)]) == 1 and j not in visited]
        if not next_cities:
            break
        current_city = next_cities[0]
        tour.append(current_city)
    tour.append(0)  # returning to the depot
    total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
else:
    print("No optimal solution found.")