import pulp
import math
import itertools

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

# Distance matrix
costs = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the problem
prob = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective
prob += pulp.lpSum(costs[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
for i in cities:
    prob += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1, "Outgoing_from_%s" % i
    prob += pulp.lpSum(x[(j, i)] for j in cities if i != j) == 1, "Incoming_to_%s" % i

# Apply subtour elimination constraints
subsets = sum([list(itertools.combinations(cities, r)) for r in range(3, n+1)], [])
for subset in subsets:
    for i in subset:
        prob += pulp.lpSum(x[(i, j)] for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
visited = set(tour)
while len(tour) < n:
    current = tour[-1]
    next_cities = [j for j in cities if j not in visited and pulp.value(x[(current, j)]) == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        visited.add(next_city)

tour.append(0)  # Return to the depot

# Calculate total cost
total_cost = sum(costs[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")