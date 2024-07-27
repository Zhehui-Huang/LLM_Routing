import pulp
import math

# City coordinates
city_coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Number of groups
n_groups = len(city_groups)
n_cities = len(city_coords)

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((city_coords[c1][0] - city_coords[c2][0])**2 + (city_coords[c1][1] - city_coords[c2][1])**2)

# Create the LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n_cities) for j in range(n_cities) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(distance(i, j) * x[(i, j)] for i in range(n_cities) for j in range(n_cities) if i != j)

# Edit constraints according to the groups
# Ensure all nodes within each group are connected to one node from another group
for group in city_groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(n_cities) if j not in group) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(n_cities) if j not in group) == 1

# Flow conservation
for i in range(n_cities):
    prob += pulp.lpSum(x[(i, j)] for j in range(n_cities) if j != i) == pulp.lpSum(x[(j, i)] for j in range(n_cities) if j != i)

# Subtour elimination (add more variables and constraints)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n_cities)), lowBound=0, upBound=n_cities-1, cat='Integer')
for i in range(1, n_cities):
    for j in range(1, n_cities):
        if i != j:
            prob += u[i] - u[j] + (n_cities - 1) * x[(i, j)] <= (n_cities - 2)
        
# Solve the problem
prob.solve()

# Extract tour
tour = []
total_cost = 0
for i in range(n_cities):
    for j in range(n_cities):
        if i != j and pulp.value(x[(i, j)]) == 1:
            tour.append((i, j))
            total_cost += distance(i, j)

# Reconstruct ordered tour
ordered_tour = [0]
while len(ordered_tour) < len(tour) + 1:
    for i, j in tour:
        if i == ordered_tour[-1]:
            ordered_tour.append(j)
            break

# Output
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)