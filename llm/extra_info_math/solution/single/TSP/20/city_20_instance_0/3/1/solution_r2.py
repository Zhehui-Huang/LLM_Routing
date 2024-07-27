import pulp
import math

# Define the city coordinates precisely
city_coords = [
    (8, 11),  # Depot city
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46),
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(city_coords)  # Number of cities including depot

# Function to calculate the Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
c = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Create the LP optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] = 1 if traveling from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective: Minimize the travel cost
model += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints: Enter and leave each city exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1

# Subtour elimination using the MTZ formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Retrieve the solution
tour = []
current_city = 0
next_city = None
for _ in range(n):
    tour.append(current_city)
    next_city = [j for j in range(n) if pulp.value(x[current_city, j]) == 1][0]
    current_city = next_city

# Close the tour
tour.append(tour[0])

# Calculate the travel cost
total_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)