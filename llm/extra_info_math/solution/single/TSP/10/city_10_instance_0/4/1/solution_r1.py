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

# Subtour elimination constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i, j)] + x[(j, i)] <= 1

# Solve the model
status = model.solve()

# Check if the model is solved
if status == pulp.LpStatusOptimal:
    # Extract tour
    path = [0]
    current = 0
    while len(path) < n:
        next_city = [j for j in range(n) if j != current and x[(current, j)].varValue == 1][0]
        path.append(next_city)
        current = next_city
    path.append(path[0])  # Return to the starting point

    # Calculate the total cost of the tour
    total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path)-1))

    # Print the outputs
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")