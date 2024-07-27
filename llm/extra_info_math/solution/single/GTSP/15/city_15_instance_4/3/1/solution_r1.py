import pulp
import math

cities = {
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

city_groups = {
    0: [0, 3, 8],
    1: [0, 4, 13],
    2: [0, 1, 2],
    3: [0, 6, 14],
    4: [0, 5, 9],
    5: [0, 7, 12],
    6: [0, 10, 11]
}

# Include depot in all group sets for modeling purposes

# Calculate Euclidean distance between cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create problem instance
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create variable x_ij
x = pulp.LpVariable.dicts("x", ((i,j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Group constraints
for group in city_groups:
    group_cities = city_groups[group]
    prob += pulp.lpSum([x[i, j] for i in group_cities for j in cities if i != j and j not in group_cities]) == 1
    prob += pulp.lpSum([x[j, i] for i in group_cities for j in cities if i != j and j not in group_cities]) == 1

# Flow conservation
for k in cities:
    prob += pulp.lpSum(x[i, k] for i in cities if i != k and (i, k) in x) == pulp.lpSum(x[k, j] for j in cities if j != k and (k, j) in x)

# Solve problem
prob.solve()
print("Status:", pulp.LpStatus[prob.status])

# Output results
tour = []
current_city = 0
visited = set()
while True:
    next_cities = [j for j in cities if j != current_city and (current_city, j) in x and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    visited.add(next_city)
    tour.append(next_city)
    current_city = next_city

# Include depot in tour
tour = [0] + tour + [0]
tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", tour_a_cost)