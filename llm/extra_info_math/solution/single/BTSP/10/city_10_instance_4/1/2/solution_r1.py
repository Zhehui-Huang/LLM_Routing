import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD

# Define the cities and their coordinates
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Number of cities including the depot
n = len(coordinates)

# Calculates Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances between all pairs of cities
distances = {
    (i, j): distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Create the problem variable:
prob = LpProblem("TSP", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)

# Maximal distance variable
max_d = LpVariable("max_d", lowBound=0, cat='Continuous')

# Objective function
prob += max_d

# Constraint: Enter and leave each city once
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination:
for S in range(2, n):
    for subset in itertools.combinations(range(n), S):
        prob += lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Constraints for maximum distance in the route
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distances[(i, j)] <= max_d

# Solve the problem using CBC (default solver)
prob.solve(PULP_CBC_CMD(msg=False))

# Extract the tour from the solution:
tour = []
current_city = 0
next_cities = list(range(n))

while len(next_cities) > 1:
    for next_city in next_cities:
        if x[(current_city, next_city)].varValue == 1:
            tour.append(current_city)
            next_cities.remove(current_city)
            current_city = next_city
            break
tour.append(0)  # Return to the depot

# Calculate total cost and maximum distance:
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")