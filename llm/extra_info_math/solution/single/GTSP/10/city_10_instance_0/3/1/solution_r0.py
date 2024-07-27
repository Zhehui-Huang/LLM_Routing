import pulp
import math

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Grouping of cities
groups = {0: [1, 2, 6], 1: [3, 7, 8], 2: [4, 5, 9]}

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# All possible one to one routes
routes = [(i, j) for i in cities for j in cities if i != j]

# Create the optimization problem
prob = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the route from city i to city j is chosen
x = pulp.LpVariable.dicts("route", (cities.keys(), cities.keys()), 
                          cat='Binary', lowBound=0, upBound=1)

# Objective: Minimize total distance
prob += pulp.lpSum(x[i][j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Shelter visit constraints, ensure each group has exactly one outgoing and one incoming connection to/from other groups
for k, v in groups.items():
    prob += pulp.lpSum(x[i][j] for i in v for j in cities if j not in v) == 1
    prob += pulp.lpSum(x[i][j] for j in v for i in cities if i not in v) == 1

# Flow conservation constraints
for i in cities:
    prob += pulp.lpSum(x[i][j] for j in cities if i != j) - pulp.lpSum(x[j][i] for j in cities if i != j) == 0

# Subtour elimination (only feasible manually for small sets or using additional variables and constraints; treating in compact form)
# Additional subtour prevention constraints
u = pulp.LpVariable.dicts('u', range(max(cities)+1), lowBound=0, cat='Continuous')
k = len(groups) + 1
for i in range(1, max(cities) + 1):
    for j in range(1, max(cities) + 1):
        if i != j:
            prob += u[i] - u[j] + k*x[i][j] <= k-1

# Solve the problem using a suitable solver
solver = pulp.PULP_CBC_CMD(msg=0) # Silent mode
prob.solve(solver)

# Extract solution
tour = []
visited = {key: False for key in cities}
current = 0
travel_cost = 0

while True:
    tour.append(current)
    visited[current] = True
    choices = [(j, x[current][j].varValue) for j in cities if current != j]
    next_city = next(j for j, val in choices if val == 1)
    travel_cost += distance(current, next_city)
    if next_city == 0:
        tour.append(next_city)
        break
    current = next_city

# Output the tour and total cost
print("Tour:", tour)
print("Total travel cost:", round(travel_cost, 2))