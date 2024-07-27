import pulp
import math

# Define the city coordinates
city_coords = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Define groups of cities
group_cities = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((city_coords[c1][0] - city_coords[c2][0])**2 + (city_coords[c1][1] - city_coords[c2][1])**2)

# Initialize the model
model = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Decision Variables
x = {}
for i in city_coords:
    for j in city_coords:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective function: minimize the total cost
model += pulp.lpSum(distance(i, j) * x[i, j] for i in city_coords for j in city_coords if i != j)

# Constraints

# Each group must have exactly one outgoing and one incoming connection
for group, cities in group_cities.items():
    model += pulp.lpSum(x[i, j] for i in cities for j in city_coords if j not in cities) == 1
    model += pulp.lpMup(x[j, i] for i in cities for j in city_coords if j not in cities) == 1

# Subtour elimination constraints
u = {}
for p in range(1, len(city_coords)):
    u[p] = pulp.LpVariable(f"u_{p}", lowBound=0, cat=pulp.LpContinuous)

k = len(city_coords)  # Number of cities
for p in range(1, len(city_coords)):
    for q in range(1, len(city_coords)):
        if p != q:
            model += u[p] - u[q] + k * pulp.lpSum(x[i, j] for i in group_cities.get(p-1, []) for j in group_cities.get(q-1, [])) + (k - 2) * pulp.lpSum(x[j, i] for i in group_cities.get(q-1, []) for j in group_cities.get(p-1, [])) <= k - 1

# Solve the model
model.solve()

# Output results
tour = [0]
total_cost = 0
current = 0
visited = set([0])
while True:
    next_city = None
    for j in city_coords:
        if j not in visited and pulp.value(x[current, j]) == 1:
            next_city = j
            break
    if next_city is None:
        break
    tour.append(next_city)
    total_cost += distance(current, next_city)
    visited.add(next_city)
    current = next_city
tour.append(0)  # Return to the depot
total_cost += distance(current, 0)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)