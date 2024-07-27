import math
import pulp

# City coordinates
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Calculating distances
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

distances = {}
for i in city_coords.keys():
    for j in city_coords.keys():
        if i != j:
            distances[(i, j)] = calculate_distance(city_coords[i], city_coords[j])

# LP Model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decisions variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coords for j in city_coords if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(distances[i, j] * x[i, j] for i in city_coords for j in city_coords if i != j)

# Constraints

# Each group must connect to at least one non-group city
for group in city_groups:
    model += pulp.lpSum(x[i, j] for j in group for i in city_coords if i not in group) == 1

# Each group must receive connection from at least one non-group city
for group in city_groups:
    model += pulp.lpSum(x[j, i] for j in group for i in city_coords if i not in group) == 1

# Flow conservation
for i in city_coords:
    if i != 0:
        model += (pulp.lpSum(x[j, i] for j in city_coords if i != j) -
                  pulp.lpSum(x[i, k] for k in city_coords if i != k) == 0)

# Solution
status = model.solve()

# Check if a valid solution is found
if status != 1:
    print("Problem cannot be solved.")
else:
    tour = []
    current_city = 0
    while True:
        next_cities = [j for j in city_coords if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
        if current_city == 0:
            break

    # Including the start back to the tour
    tour.insert(0, 0)
    # Calculate cost
    total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)