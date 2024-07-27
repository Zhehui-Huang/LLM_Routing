import math
import pulp

# Coordinates of cities
cities = {
    0: (53, 68),  # depot
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
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Initialize the model
model = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables: x_ij = 1 if route i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')

# Subtour elimination vars
u = pulp.LpVariable.dicts("u", range(1, len(cities)), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints
for group_idx, group in groups.items():
    model += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

for c in cities:
    model += pulp.lpSum(x[(i, c)] for i in cities if i != c) - pulp.lpSum(x[(c, j)] for j in cities if j != c) == 0

k = 10
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + k * x[(i, j)] <= k - 1
  
# Solve the model
model.solve()

# Extract the tour
tour = [0]
current = 0
while len(tour) < len(groups) + 1:
    for j in cities:
        if j != current and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
            current = j
            break
tour.append(0)

# Calculate the cost of the tour
tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", round(tour_cost, 2))