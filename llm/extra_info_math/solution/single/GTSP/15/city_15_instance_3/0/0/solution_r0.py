import pulp
import math

# Define the cities and their coordinates
coords = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Define groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Initialize Linear Programming model
model = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in coords for j in coords if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, len(city_groups) + 1), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in coords for j in coords if i != j)

# Constraints
for k, group in enumerate(city_groups, 1):
    model += pulp.lpSum(x[i, j] for i in group for j in set(coords.keys()) - set(group)) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in set(coords.keys()) - set(group)) == 1

# Flow conservation
for i in coords:
    model += pulp.lpSum(x[j, i] for j in coords if j != i) - pulp.lpSum(x[i, j] for j in coords if i != j) == 0

# Subtour elimination
for k in range(1, len(city_groups)):
    for l in range(k + 1, len(city_groups) + 1):
        for i in city_groups[k-1]:
            for j in city_groups[l-1]:
                model += u[k] - u[l] + len(city_groups) * x[i, j] + (len(citygroups)-2) * x[j, i] <= len(city_groups) - 1

# Solve the problem
status = model.solve()

if status == pulp.LpStatusOptimal:
    tour = [0]
    current_city = 0
    visited = {0}
    while len(visited) < len(coords):
        for next_city in coords:
            if next_city != current_city and pulp.value(x[current_city, next_city]) == 1:
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city
                break
    tour.append(0)  # return to depot
    total_cost = pulp.value(model.objective)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Optimal tour could not be found!")