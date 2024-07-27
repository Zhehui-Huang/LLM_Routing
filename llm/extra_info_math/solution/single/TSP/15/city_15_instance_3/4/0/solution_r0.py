import pulp
import math

# Coordinates for the depot and other cities
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50),
    (35, 73), (42, 64), (64, 30), (70, 95),
    (29, 64), (32, 79)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Number of cities (including depot)
n = len(coordinates)

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective Function: Minimize the sum of distances for the tour
prob += pulp.lpSum([euclidean_distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints: Each city is visited exactly once
for i in range(n):
    prob += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1  # Leave city `i` exactly once
    prob += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1  # Enter city `i` exactly once

# Subtour Elimination via the MTZ constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the optimal tour and calculate its total distance
tour = []
current_city = 0
start = 0

# Follow x from the depot and onward
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current and current_city, j]) == 1]
    if not next_cities:  # No outgoing edges found (should not happen)
        break
    current_city = next_cities[0]
    if current_city == start:
        break

# Close the loop for the tour
tour.append(start)

# Calculate the total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")