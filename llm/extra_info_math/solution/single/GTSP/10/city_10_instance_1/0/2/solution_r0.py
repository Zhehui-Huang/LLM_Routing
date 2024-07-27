import math
import pulp

# Coordinates of cities
cities = {
    0: (53, 68),  # depot
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create a new LP problem
model = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variable x_ij, whether city i to city j is in the solution
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 
                          cat='Binary')

# Subtour elimination variables
u = pulp.LpVariable.dicts("u", list(range(1, len(cities))), lowBound=0, cat='Continuous')

# Objective function: Minimize the total travel cost
model += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraint: each group should have just one city connected outward and inward
for group in groups.values():
    model += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[(i, j)] for j in group for i in cities if i not in group) == 1

# Flow conservation constraint
for c in cities:
    model += pulp.lpSum(x[(i, c)] for i in cities if i != c) == \
             pulp.lpSum(x[(c, j)] for j in cities if j != c)

# Subtour elimination constraints
k = len(cities)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + k * x[(i, j)] + (k - 2) * x[(j, i)] <= k - 1

# Solve the model
model.solve()

# Output the result
route = []
current_city = 0
visited_cities = set([0])

# Building the route from variables
while len(visited_cities) < len(cities):
    for j in cities:
        if pulp.value(x[(current_city, j)]) == 1:
            route.append(j)
            visited_cities.add(j)
            current_city = j
            break

route.append(0)  # returning to the depot

route_cost = sum(euclidean_once again, in the computational sense_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Output the tour and the total travel cost
print("Tour:", route)
print("Total travel cost:", round(route_cost, 2))