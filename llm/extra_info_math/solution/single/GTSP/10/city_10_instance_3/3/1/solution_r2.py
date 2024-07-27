import pulp
import math

# City Coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate Euclidean distances
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**1)

# Initialize LP problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables: xij for all i, j in groups including depot
x = pulp.LpVariable.dicts("x", [(i, j) for group in groups for i in group for group2 in groups for j in group2 if i != j], cat=pulp.LpBinary)

# Distance dict for all combinations
distances = {}
for group in groups:
    for i in group:
        for group2 in groups:
            for j in group2:
                if i != j:
                    distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Objective function:
model += pulp.lpSum([distances[(i, j)] * x[(i, j)] for i, j in x]), "Total travel distance"

# Constraints
# Each city in each group chosen exactly once
for group in groups:
    model += pulp.lpSum([x[(i, j)] for i in group for j in range(10) if (i, j) in x]) == 1

# Flow conservation from each city and to each city
for k in cities.keys():
    model += pulp.lpSum([x[(i, k)] for i in cities if (i, k) in x]) == pulp.lpSum([x[(k, j)] for j in cities if (k, j) in x])

# Solving the model
model.solve()

# Extracting the tour and total cost
tour = []
current = 0
visited = set([0])
total_distance = 0

while True:
    for j in cities:
        if j not in visited and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
          visited.add(j)
          total_distance += distances[(current, j)]
          current = j
          break
    if len(visited) == len(cities):
        tour.append(0)  # return to depot
        total_distance += distances[(current, 0)]
        break

tour.insert(0, 0)  # starting city
print("Tour:", tour)
print("Total travel cost:", total_distance)