import pulp
import math

# Coordinates of cities (indexed from 0)
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(coordinates)
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] = 1 if route from city i to city j is chosen, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: Minimize the sum of distances for included edges in the tour
problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# Each city must be left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination constraints - Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1)*x[i, j] <= n-2

# Solve the problem
problem.solve()

# Retrieve the optimal route and its cost
tour = []
current_city = 0
while True:
    # Find the next city with x[current_city, j] = 1
    next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

# Include the depot as start and end
tour = [0] + tour

# Calculate total travel cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")