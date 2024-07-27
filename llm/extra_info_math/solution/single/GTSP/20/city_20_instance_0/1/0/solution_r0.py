import pulp
import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates, including the depot
coordinates = [
    (8, 11),   # Depot
    (40, 6),   (95, 33),   (80, 60),   (25, 18),   (67, 23),
    (97, 32),  (25, 71),   (61, 16),   (27, 91),   (91, 46),
    (40, 87),  (20, 97),   (61, 25),   (5, 59),    (62, 88),
    (13, 43),  (61, 28),   (60, 63),   (93, 15)
]

city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Number of cities
n_cities = len(coordinates)

# Calculate distances
distances = {(i, j): euclidean_istance(coordinates[i], coordinates[j])
             for i in range(n_cities) for j in range(n_cities) if i != j}

# Create problem variable
problem = pulp.LpProblem("TSP_Subtour_Problem", pulp.LpMinimize)

# Create variable (x_ij - binary variable for travel between cities)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n_cities) for j in range(n_cities) if i != j),
                          cat=pulp.LpBinary)

# Create the objective function
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in range(n_cities) for j in range(n_cities) if i != j])

# Constraints for ensuring exactly one city from each group is visited
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(n_cities) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in range(n_cities) if i != j) == 1

# Flow conservation constraint
for i in range(n_cities):
    problem += pulp.lpSum(x[i, j] for j in range(n_cities) if i != j) - pulp.lpSum(x[j, i] for j in range(n_cities) if i != j) == 0

# Solve the problem
problem.solve()

# Get the solution
tour = []
for v in problem.variables():
    if v.varValue > 0 and v.name.startswith('x'):
        _, indices = v.name.split('_')[1].split('(')[1].split(')')[0].split(',')
        tour.append((int(indices.split(',')[0]), int(indices.split(',')[1])))

# To extract the path from the tour variable
path = [0]
while len(path) < len(city_groups) + 1:
    for a, b in tour:
        if a == path[-1]:
            path.append(b)
            break

# Include the path back to the depot
path.append(0)

# Calculate and print the results
total_distance = sum(distances[path[i], path[i + 1]] for i in range(len(path) - 1))

print("Tour:", path)
print("Total travel cost:", total_distance)