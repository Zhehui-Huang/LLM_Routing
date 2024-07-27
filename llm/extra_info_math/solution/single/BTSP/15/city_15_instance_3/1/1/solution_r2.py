import pulp
import math
import itertools

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n = len(cities)  # Total cities

# Define problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective: Minimize the longest edge in the tour
prob += z

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # Exactly one outgoing edge from each city
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # Exactly one incoming edge to each city

# Max distance constraints
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * calc_distance(i, j) <= z

# Subtour Elimination Constraints (SECs)
for S in range(3, n):
    for subset in itertools.combinations([i for i in range(1, n)], S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve problem
prob.solve()

# Retrieve solution if optimal
if prob.status == pulp.LpStatusOptimal:
    edges = [(i, j) for i in cities for j in cities if i != j and x[i, j].varValue > 0.99]

    # Construct tour from edges
    tour = [0]
    while len(tour) < n:
        last = tour[-1]
        next_city = [j for i, j in edges if i == last][0]
        tour.append(next_city)
        edges.remove((last, next_city))

    # Closing the tour
    tour.append(0)

    total_distance = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_leg_distance = max(calc_latte_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", round(total_distance, 2))
    print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))
else:
    print("Solution is not optimal or computable.")