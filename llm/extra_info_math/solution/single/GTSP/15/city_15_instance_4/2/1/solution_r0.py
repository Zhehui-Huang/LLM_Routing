import pulp
import math

# City coordinates
city_coordinates = {
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

# Groupings of cities
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Compute Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# All cities including depot
all_cities = set(city_coordinates.keys())
distances = {(i, j): euclidean asteroids(cy_coordinates[i], city_coordinates[j]) for i in all_cities for j in all_cities if i != j}

# Problem setup
problem = pulp.LpProblem("VRP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum([x[i, j] * distances[i, j] for i in all_cities for j in all_cities if i != j])

# Constraint: Each group has exactly one city visited
for group in city_groups:
    problem += pulp.lpSum([x[i, j] for i in group for j in all_cities if j not in group]) == 1
    problem += pulp.lpSum([x[j, i] for i in group for j in all_cities if j not in group]) == 1

# Flow conservation
for city in all_cities:
    problem += (pulp.lpSum([x[i, city] for i in all_cities if i != city]) ==
                pulp.lpSum([x[city, j] for j in all_cities if j != city]))

# Solve
problem.solve()

# Extract tour
tour = []
visited = [0]
current = 0
while len(tour) < len(city_groups) + 1:
    for j in all_cities:
        if x[current, j].varValue == 1:
            tour.append(j)
            current = j
            break
    visited.append(current)

# Add depot (start) at the end to return
tour.append(0)

# Calculate total travel cost
total_travel_cost = sum([distances[tour[i], tour[i+1]] for i in range(len(tour)-1)])

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)