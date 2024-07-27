import pulp
import math

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

# Constraints:
# Enter each city exactly once.
for j in cities:
    model += sum(x[(i, j)] for i in cities if i != j) == 1

# Leave each city exactly once.
for i in cities:
    model += sum(x[(i, j)] for j in cities if i != j) == 1

# Subtour Elimination Constraints
for k in range(3, len(cities) + 1):
    for subset in itertools.combinations(cities, k):
        model += sum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = model.solve()

# Check if the optimal solution was found
if status != pulp.LpStatusOptimal:
    print("Failed to find an optimal solution.")
else:
    # Extract the tour from the variables
    tour = []
    current_city = 0
    next_city = None
    total_cost = 0

    while True:
        tour.append(current_city)
        next_city = next(j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1)
        total_cost += calculate_foristance(current_city, next_city)
        if next_city == 0:
            break
        else:
            current_city = next_city

    # Output the results
    tour.append(0)  # append the return to the depot

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")