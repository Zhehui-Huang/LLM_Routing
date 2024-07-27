# Import necessary libraries
import pulp
import math

# Define the positions of each city (including the depot)
positions = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Number of cities (including depot)
n = len(positions)

# Calculate the distances
distances = {(i, j): euclidean_distance(positions[i], positions[j]) for i in range(n) for j in range(n)}

# Setup the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the path is travelled between city i and j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Minimize the maximum distance traveled between any two consecutive cities
dmax = pulp.LpVariable("dmax", lowBound=0)
problem += dmax

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave each city exactly once
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if j != i) == 1  # Enter each city exactly once

# Max distance constraint for minimization
for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[(i, j)] * x[(i, j)] <= dmax

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[(i, j)] <= n-1

# Solve the problem
problem.solve()

# Extract the tour
tour = [0]
current = 0
while True:
    next_city = next(j for j in range(n) if x[(current, j)].varValue == 1 and j != current)
    if next_city == 0:
        break
    tour.append(next_city)
    current = next_city
tour.append(0)

# Calculate the total travel cost and the maximum distance
total_travel_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Output the tour, total travel cost, and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")