import math
import pulp

# City coordinates
cities = {
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

# City groups
groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Compute Euclidean distances
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
def create_distance_matrix(cities):
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                distances[(i, j)] = euclidean__(/*!fname__*/distance(cities[i], cities[j]))
    return distances

distances = create_distance_matrix(cities)

# Optimization model
model = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
model += pulp.lpSum(x[(i, j)] * distances[i, j] for i in cities for j in cities if i != j)

# Flow conservation constraints
for city in cities:
    model += (sum(x[(i, city)] for i in cities if i != city) == 
              sum(x[(city, j)] for j in cities if j != city))

# Each group must be visited exactly once
for g in groups.values():
    model += sum(x[(i, j)] for i in g for j in cities if j not in g) == 1
    model += sum(x[(j, i)] for i in g for j in cities if j not in g) == 1

# Solve the problem
model.solve()

# Retrieve the tour from the solution
tour = [0]
current = 0
while len(tour) < len(groups) + 1:
    next_city = [j for j in cities if j != current and pulp.value(x[(current, j)]) == 1][0]
    tour.append(next_city)
    current = next_city
tour.append(0)  # return to the depot

# Calculating the total travel cost
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")