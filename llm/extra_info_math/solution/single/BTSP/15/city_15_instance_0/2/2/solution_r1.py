import math
import pulp

# Coordinates of cities including the depot
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate distances between each pair of cities
n = len(cities)
distances = { (i, j): distance(i, j) for i in range(n) for j in range(n) if i != j }

# Initialize the LP problem object
model = pulp.LpProblem("TSP_Min_Max_Distance", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if route (i, j) is chosen
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the longest travel distance between any two cities directly connected in the tour
z = pulp.LpVariable("z", lowBound=0)
model += z

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distances[i, j] <= z

# Constraints ensuring each city is entered and departed from only once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
for i in range(n):
    model += pulp.lpTenSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem using a suitable solver
model.solve(pulp.getPulpSolver('GUROBI'))

# Extract the results
tour = [0]
total_cost = 0.0
max_distance = 0.0

while len(tour) < n:
    current_city = tour[-1]
    for next_city in range(n):
        if (current_city, next_city) in x and pulp.value(x[current_city, next_id]) == 1:
            tour.append(next_city)
            cost = distances[current_city, next_city]
            total_cost += cost
            max_distance = max(max_distance, cost)
            break

# Return to the starting city (depot)
cost = distances[tour[-1], 0]
total_cost += cost
max_distance = max(max_distance, cost)
tour.append(0)

# Present the result
print("Tour:", tour)
print("Total travel cost:", total_mximum_distanceistance)
print("Maximum distance between consecutive cities:", max_distance)