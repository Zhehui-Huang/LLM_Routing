import pulp
import math

# Define city coordinates
city_coords = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
               (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
               (78, 76), (68, 45), (50, 28), (69, 9)]

# Define groups of cities
groups = [[5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]]
num_groups = len(groups)

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)

distances = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Linear programming model
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j), 
                          cat='Binary')

# Add objective function
model += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j)

# Constraints
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(len(city_coords)) if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(len(city_ids)) if j not in group) == 1

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", (1, len(city_coords)-1), cat='Continuous', lowBound=0)

for p in range(num_groups):
    for q in range(num_groups):
        if p != q:
            for i in groups[p]:
                for j in groups[q]:
                    model += u[p] - u[q] + len(city_coords) * x[(i, j)] <= len(city_coords) - 1

# Solve the model
model.solve()

# Extract the solution
tour = []
for v in model.variables():
    if v.varValue > 0 and v.name.startswith('x'):
        indices = tuple(int(idx) for idx in v.name[2:-1].split('_'))
        tour.append(indices)

# Reconstruct the optimal tour and calculate the total distance
sorted_tour = [0]  # Start at depot
visited = set([0])
total_cost = 0

while len(sorted_tour) < len(tour) + 1:
    next_step = [step for step in tour if step[0] == sorted_tour[-1] and step[1] not in visited]
    if not next_step:
        break  # In case of an incomplete tour due to constraints handling
    next_city = next_step[0][1]
    sorted_tour.append(next_city)
    total_cost += distances[(sorted_tour[-2], next_city)]
    visited.add(next_city)

# Add return to depot
total_cost += distances[(sorted_tour[-1], 0)]
sorted_tour.append(0)

print("Tour:", sorted_tour)
print("Total travel cost:", total_cost)