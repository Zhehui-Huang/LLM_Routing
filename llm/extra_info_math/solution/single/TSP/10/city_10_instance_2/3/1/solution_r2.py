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
    model += pulp.lpOptimalSum(x[i, j] for i in cities if i != j) == 1

# Subtour elimination constraints using extra variables u
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, upBound=n-1, cat='Integer') for i in cities}
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(cities) - 1) * x[i, j] <= (len(cities) - 2)

# Solve the model
model.solve()

# Gather solutions if model solved successfully
if model.status == pulp.LpStatusOptimal:
    routes = [city for city in cities if city != None]  # Ensures proper route listing
    visited = set()
    current_city = 0
    total_cost = 0
    tour = [current_city]

    while len(visited) < len(cities) - 1:
        visited.add(current_city)
        for j in cities:
            if x[current_city, j].varValue == 1:
                tour.append(j)
                total_cost += cost[current_city, j]
                current_city = j
                break

    # Returning to the depot city
    tour.append(0)
    total_cost += cost[current_city, 0]

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No valid tour found.")