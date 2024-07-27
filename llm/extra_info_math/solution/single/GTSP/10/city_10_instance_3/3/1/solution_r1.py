import pulp
import math

# Define city coordinates
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

# Define groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Initialize the optimization model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables x_ij = 1 if path from city i to city j is chosen
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective: Minimize the total distance
model += pulp.lpSum(distances[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in distances)

# Constraints to ensure each group has exactly one node visited
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1  # exit constraint
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1  # entry constraint

# Flow conservation constraint to maintain continuity in the tour
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if j != i and (i, j) in distances) == \
             pulp.lpSum(x[j, i] for j in cities if j != i and (j, i) in distances), f"Continuity_at_node_{i}"

# Solve the model
model.solve()

# Retrieve the tour and calculate the cost
tour = [0]  # start at depot
visited = set([0])

# Start at the depot and build the tour
current_city = 0
total_cost = 0

while True:
    found = False
    for j in cities:
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            next_city = j
            tour.append(next_city)
            total_cost += distances[current_city, next_city]
            current_city = next_city
          visited.add(next_city)
          found = True
          break
    if not found or current_city == 0:
        break

tour.append(0)  # end at the depot
total_cost += distances[current_city, 0]  # add cost to return to the depot

print("Tour:", tour)
print("Total travel cost:", total_cost)