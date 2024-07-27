import pulp
import math
import itertools

# Define the cities and their locations
locations = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
             (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Calculate distances between all pairs of cities
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

distances = {}
n = len(locations)
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(locations[i], locations[j])

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
for k in range(n):
    prob += pulp.lpSum([x[(k, j)] for j in range(n) if k != j]) == 1
    prob += pulp.lpSum([x[(i, k)] for i in range(n) if i != k]) == 1

# Subtour elimination constraints
for m in range(2, n):
    for subset in itertools.combinations(range(1, n), m):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour and calculate the total distance
tour = [0]
current_location = 0
total_cost = 0

while len(tour) < n:
    next_location = next(j for j in range(n) if x[current_location, j].varValue == 1)
    total_cost += distances[(current_location, next_location)]
    tour.append(next_location)
    current_location = next_location

# Close the tour
tour.append(0)
total_cost += distances[(current_location, 0)]

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)