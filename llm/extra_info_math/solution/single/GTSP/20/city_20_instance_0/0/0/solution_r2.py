import pulp
from math import sqrt

# Define the city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# City groups:
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize the optimization problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables for paths between cities
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective Function: Minimize the sum of the distances
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Flow conservation constraints
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) - pulp.lpSum(x[j, i] for j in cities if j != i) == 0

# Solve the model
model.solve()

# Extract solution
path = []
current = 0
path.append(current)
count = 0
while True:
    next_city = [j for j in cities if pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    current = next_city[0]
    path.append(current)
    if current == 0:
        break
    count += 1
    if count > 50: # to prevent infinite loops if there's an error
        break

total_distance = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))

# Output results
print("Tour:", path)
print("Total travel cost:", total_distance)