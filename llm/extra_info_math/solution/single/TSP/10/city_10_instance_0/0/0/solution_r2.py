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

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create the LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij where i, j are cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective: Minimize the sum of distances between consecutive cities
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints
# Every city must be left and entered exactly once
for c in cities:
    problem += pulp.lpSum(x[i, j] for i in cities for j in cities if i == c and j != i) == 1
    problem += pulp.lpSum(x[i, j] for i in cities for j in cities if j == c and i != j) == 1

# Subtour elimination
for k in range(2, len(cities)):
    for subtour in itertools.combinations(cities, k):
        problem += pulp.lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
problem.solve()

# Get the order of cities visited
if pulp.LpStatus[problem.status] == 'Optimal':
    edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[i, j]) == 1]
    tour = [0]
    while len(edges) > 0:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                edges.remove((i, j))
                break
    tour.append(tour[0]) # Return to the depot

    # Calculate total travel cost
    total_travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
else:
    print("Failed to find an optimal solution.")