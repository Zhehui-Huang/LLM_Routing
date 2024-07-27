import math
import pulp

# Define city coordinates
city_coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Calculate the distance matrix
n = len(city_coordinates)
distances = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Create the model
model = pulp.LpProblem('TSP', pulp.LpMinimize)

# Decision variables: x[i][j] = 1 if travel from i to j
x = {
    (i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
    for i in range(n)
    for j in range(n)
    if i != j
}

# Objective: Minimize the sum of travel distances
model += pulp.lpSum(x[i, j] * distances[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Leave each city only once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Enter each city only once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination (implemented using Miller-Tucker-Zemlin constraints)
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the model
status = model.solve()

# Extract the tour
tour = []
current = 0
while True:
    tour.append(current)
    next_moves = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_votes:
        break
    current = next_votes[0]

tour.append(0)  # returning to the depot
total_cost = pulp.value(model.objective)

# Output the results
print('Tour: ', tour)
print('Total travel cost: ', total_cost)