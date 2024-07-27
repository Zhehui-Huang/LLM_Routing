import pulp
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

cost = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Number of cities
n = len(cities)

# Create the integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective function
model += pulp.lpSum(cost[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
# Each city is left exactly once
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1

# Each city is entered exactly once
for j in cities:
    model += pulp.lpSum(x[i, j] for i in cities if i != j) == 1

# Subtour elimination constraints using extra variables u
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, upBound=n-1, cat='Integer') for i in cities}
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Check if a valid solution was found
if model.status == 1:
    # Extract the tour
    tour = []
    current_city = 0
    visited = [False] * n
    total_cost = 0

    while True:
        tour.append(current_city)
        visited[current_city] = True
        next_city = None
        for j in cities:
            if j != current_city and pulp.value(x[current_city, j]) == 1:
                next_city = j
                total_cost += cost[current_city, j]
                break
        if next_city == 0:  # if returning back to the depot city
            tour.append(next_city)
            total_cost += cost[current_city, next|_city]
            break
        else:
            current_city = next_city

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No valid tour found.")