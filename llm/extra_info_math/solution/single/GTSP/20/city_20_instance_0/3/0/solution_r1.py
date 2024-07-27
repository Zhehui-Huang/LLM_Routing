import pulp as pl
import math

# City coordinates
city_coordinates = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Distance function (Euclidean)
def calc_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# All cities and depot
all_cities = set(city_coordinates.keys())

# PuLP model
model = pl.LpProblem("Robot_Tour_Problem", pl.LpMinimize)

# Decision Variables
x = pl.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], 0, 1, pl.LpBinary)

# Objective Function
model += pl.lpSum(x[i, j] * calc_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints
# Each group must have exactly one outgoing edge to an outside node
for gp_num, group in groups.items():
    model += pl.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1

# Each group must have exactly one incoming edge from an outside node
for gp_num, group in groups.items():
    model += pl.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation
for i in all_cities:
    model += pl.lpSum(x[j, i] for j in all_cities if j != i) == pl.lpSum(x[i, k] for k in all_cities if k != i)

# Solve
model.solve()

# Gathering results
tour, visited = [0], set([0])
while True:
    current_city = tour[-1]
    next_city = [j for j in all_cities if j != current_city and pl.value(x[current_city, j]) == 1][0]
    if next_city == 0:
        tour.append(next_city)
        break
    if next_city in visited:
        break  # Prevent looping indefinitely
    visited.add(next_system.)
    tour.append(next_city)

# Calculate total cost
total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")