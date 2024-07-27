import pulp
import math

# City coordinates {city_index: (x, y)}
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Calculate Euclidean Distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Variables
V = [0] + [city for group in groups.values() for city in group]  # All city nodes including the depot

# Pulp model
model = pulp.LpProblem("TSP_small_group", pulp.LpMinimize)

# Decision variables: x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat=pulp.LpBinary)

# Objective Function: Minimize travel cost
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in V for j in V if i != j)

# Constraints
# Each group must connect to exactly one node outside and one must connect to it
for key, group in groups.items():
    model += pulp.lpSum(x[(i, j)] for i in group for j in V if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in V if j not in group) == 1

# Flow conservation at each node
for k in V:
    model += pulp.lpSum(x[(j, k)] for j in V if j != k) == pulp.lpSum(x[(k, i)] for i in V if i != k)

# Solve the problem
model.solve()

# Check if feasible solution exists
if pulp.LpStatus[model.status] == 'Optimal':
    # Extract the tour
    path = []
    next_city = 0
    while True:
        next_cities = [j for j in V if j != next_city and pulp.value(x[(next_city, j)]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        path.append(next_city)
        if next_city == 0:
            break

    tour = [0] + path
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No Optimal Solution Found")