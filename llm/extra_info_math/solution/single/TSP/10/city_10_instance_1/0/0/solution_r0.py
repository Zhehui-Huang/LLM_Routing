import pulp
import math

# City coordinates
cities = {
    0: (53, 68),
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

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two coordinates """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(cities)  # Number of cities

# Calculate the cost dictionary
costs = {}
for i in cities:
    for j in cities:
        if i != j:
            costs[(i, j)] = calculate_distance(cities[i], cities[j])

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')

# Objective
prob += pulp.lpSum(costs[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
for i in cities:
    prob += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in cities if j != i) == 1

# Subtour elimination
for S in range(2, n):
    for subset in itertools.combinations(cities.keys(), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_city)
    next_cities = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if next_cities:
        current_city = next_cities[0]

# Add depot city at the end of the tour
tour.append(0)

# Calculate the total travel cost
total_cost = sum(costs[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")