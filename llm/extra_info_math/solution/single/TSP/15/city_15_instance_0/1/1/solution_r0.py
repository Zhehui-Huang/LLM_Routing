import pulp
import math

# List of city coordinates (index corresponds to city number) - 0 is the depot
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities including the depot
n = len(cities)

# Create the distance matrix
cost = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Setup the optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the route goes directly from i to j
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective Function
model += pulp.lpSum([x[(i, j)] * cost[(i, j)] for (i, j) in cost.keys()]), "Total Cost"

# Constraints
# Each city must be left exactly one time
for i in range(1, n):
    model += pulp.lpSum([x[(i, j)] for j in range(n) if (i, j) in x]) == 1

# Each city must be entered exactly one time
for j in range(1, n):
    model += pulp.lpSum([x[(i, j)] for i in range(n) if (i, j) in x]) == 1

# Subtour elimination by adding constraints using dummy variables and a large M
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1)*x[(i, j)] <= n-2

# Solve the model
model.solve()

# Output results
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if (current_city, j) in x and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Retrace tour to first city (depot)
tour.insert(0, 0)  # start at depot
tour.append(0)  # end at depot

# Calculate the tour cost
total_cost = sum(cost[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")