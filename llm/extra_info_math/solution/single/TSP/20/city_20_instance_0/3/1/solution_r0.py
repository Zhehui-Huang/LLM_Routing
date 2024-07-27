import pulp
import math

# City coordinates
city_coords = [
    (8, 11),  # depot city
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), 
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
    (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(city_coords)  # number of cities including depot

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
c = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if tour goes from city i to city j, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)),
                          cat='Binary')

# Objective function: minimize total travel cost
model += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += (pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1)  # leave each city only once
    model += (pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1)  # enter each city only once

# Subtour elimination constraints
for S in range(3, n+1):
    for subset in itertools.combinations(range(1, n), S):
        model += (pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Check the status of the optimization
if status != pulp.LpStatusOptimal:
    print("Failed to obtain the optimal solution.")
    exit()

# Retrieve the tour from the solution
tour = []
visited = set()
current_city = 0
while True:
    tour.append(current_city)
    visited.add(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
    if current_city in visited:
        break

# Ensure the tour returns to the starting city (depot)
tour.append(0)

# Calculate the total travel cost
total_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)