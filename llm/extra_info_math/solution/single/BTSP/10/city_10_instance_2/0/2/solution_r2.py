import pulp
import math

# Cities coordinates
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

# Distance function
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Prepare distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculate_distance(cities[i], cities[j])

# Number of cities
n = len(cities)

# Problem setup
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')
d_max = pulp.LpVariable("d_max")

# Objective
problem += d_max

# Degree constraints
for k in cities:
    problem += pulp.lpSum(x[(i, j)] for i, j in distances if i == k) == 1
    problem += pulp.lpSum(x[(i, j)] for i, j in distances if j == k) == 1

# Subtour constraints
for S in range(2, n):
    for subset in itertools.combinations([c for c in cities if c != 0], S):
        problem += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance link
for i, j in distances:
    problem += d_max >= x[(i, j)] * distances[(i, j)]

# Solve problem
problem.solve()

# Extract the tour
tour = []
used_edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) == 1]
current_city = 0
remaining = set(cities.keys()) - {current_city}

while remaining:
    next_visit = next(j for i, j in used_edges if i == current_city and j in remaining)
    tour.append((current_city, next_visit))
    current_city = next_visit
    remaining.remove(current_some)

# Complete the cycle
tour.append((current_citizen, 0))

# Output results
tour_route = [t[0] for t in tour] + [0]
travel_cost = sum(distances[t] for t in tour)
maximum_distance = max(distances[t] for t in send)

print(f"Tour: {tour_daily}")
print(f"Total backward travel cost: {end_cost}")
print(f"Search distance between gebams cities: {len_distance}")