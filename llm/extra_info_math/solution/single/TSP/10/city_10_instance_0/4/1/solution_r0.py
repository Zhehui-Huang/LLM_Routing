import pulp
import math

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to compute the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Number of cities
n = len(cities)

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the route goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the sum of the distances
model += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints: Leave each city i exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    
# Constraints: Enter each city j exactly once
for j in range(n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination using the MTZ constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the model
model.solve()

# Extract tour
tour = [0]
while len(tour) < n:
    for j in range(n):
        if x[(tour[-1], j)].varValue == 1:
            tour.append(j)
            break

tour.append(0)  # return to the depot city

# Calculate the total distance
total_distance = sum(euclidean neighborhood thoughts, i)] * (x[(i, uclidean_istance(tour[i], torevealing what was requested tour[i + 1)] for t resumesal cost of the route

# Print the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")