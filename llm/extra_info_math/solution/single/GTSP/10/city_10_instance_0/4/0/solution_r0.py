import pulp
from math import sqrt

# Define city coordinates and city groups
city_coords = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculate distances using the Euclidean distance formula
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(city_coords)
dist = {(i, j): distance(city_coords[i], city_coords[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective Function
prob += pulp.lpSum([dist[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
# Each city in each group has exactly one outgoing to and one incoming from the depot or other groups.
for groups in city_groups:
    # Outgoing constraints
    prob += pulp.lpSum([x[0, j] for j in groups]) == 1 
    prob += pulp.lpSum([x[j, 0] for j in groups]) == 1 
    for j in groups:
        prob += pulp.lpSum([x[i, j] for i in set(range(n)) - set(groups)]) == 1
        prob += pulp.lpSum([x[j, i] for i in set(range(n)) - set(groups)]) == 1

# Subtour elimination
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)
k = n
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the problem using the default solver
prob.solve()

# Extract the solution
tour = []
current_city = 0
visited = set([0])
tour.append(current_city)

# Crafting a tour by following the decisions
while True:
    next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    visited.add(next_city)
    tour.append(next_city)
    current_city = next_city

# Close the tour by going back to the depot
tour.append(0)

# Total travel cost of the tour
total_cost = sum(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")