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

n = len(cities)  # Number of cities including the depot

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Cost matrix
cost = { (i, j): distance(i, j) for i in cities for j in cities if i != j}

# TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", cost.keys(), 0, 1, pulp.LpBinary)

# Objective function
model += pulp.lpSum(cost[i, j] * x[i, j] for i, j in cost.keys()), "Objective_Function"

# Constraints
for c in cities:
    model += pulp.lpSum(x[i, j] for i, j in cost.keys() if i == c) == 1, f"Leave_city_{c}"
    model += pulp.lpSum(x[i, j] for i, j in cost.keys() if j == c) == 1, f"Enter_city_{c}"

# Subtour constraint
for k in range(2, n):
    for subset in itertools.combinations(cities, k):
        model += pulp.lpSum(x[i, j] for i, j in cost.keys() if i in subset and j in subset) <= len(subset) - 1

# Solve the problem
model.solve()

# Output results
tour = []
current_city = 0
while True:
    next_cities = [j for (i, j) in x.keys() if i == current_city and pulp.value(x[(i, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

tour = [0] + tour
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")