import math
import pulp
import itertools

# Define the cities and their coordinates.
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

# Function to calculate Euclidean distance between two cities.
def calculate_distance(i, j):
    return math.dist(cities[i], cities[j])

# Create TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the variables: x_ij = 1 if the tour goes from city i to city j, 0 otherwise.
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function: Minimize the sum of travel distances.
model += pulp.lpSum(x[(i, j)] * calculate_distance(i, j) for i in cities for j in cities if i != j)

# Enter each city exactly once except depot (since departure and arrival happen there).
for j in cities:
    model += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1

# Leave each city exactly once except depot.
for i in cities:
    model += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1

# Subtour Elimination Constraints
for k in range(2, len(cities)):
    for subset in itertools.combinations(cities, k):
        if 0 not in subset:
            model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = model.solve()

# Result parsing and output
if status == pulp.LpStatusOptimal:
    tour = []
    total_cost = 0
    current_city = 0
    while True:
        for j in cities:
            if j != current_city and pulp.value(x[(current_city, j)]) == 1:
                tour.append(j)
                total_cost += calculate_distance(current_city, j)
                current_city = j
                break
        if current_city == 0:
            break
    tour = [0] + tour
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("An optimal tour configuration could not be found.")