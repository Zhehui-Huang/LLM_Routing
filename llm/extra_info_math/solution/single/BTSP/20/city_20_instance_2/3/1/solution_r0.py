import pulp
import math

# Define the coordinates of the cities including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

n = len(coordinates)  # Number of cities

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the variables: x[i][j] is 1 if the path goes from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat='Binary')

# Define the maximum distance variable
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += max_distance

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leaving each city
    prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1  # Entering each city

# Sub-tour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i][j] + x[j][i] <= 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i][j] <= max_distance

# Solve the problem using the default solver
prob.solve()

# Extract the tour from the variables
tour = []
current_city = 0
while True:
    next_city = next(j for j in range(n) if x[current_city][j].varValue == 1)
    tour.append(current_city)
    if next_city == 0:
        break
    current_city = next_city

tour.append(0)  # Finish at the starting city

# Calculate total cost and maximum leg distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_leg_distance, 2)}")