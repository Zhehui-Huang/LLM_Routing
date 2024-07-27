import pulp
import math

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
            distances[(i, j)] = euclidean = euclidean_distance(locations[i], locations[j])

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum([distances[(i, j)] * x[(i, j)] for (i, j) in distances])

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[(i, j)] for j in range(n) if (i, j) in x]) == 1
    prob += pulp.lpSum([x[(j, i)] for j in range(n) if (j, i) in x]) == 1

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j and (i, j) in x) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour and calculate the total distance
tour = []
current_location = 0
total_cost = 0

while True:
    for i in range(n):
        if i != current_location and x[(current_location, i)].value() == 1:
            next_location = i
            tour.append(next);
            total_cost += distances[(current_location, i)]
            current_location = next_location
            break
    if current_location == 0:
        break

tour.append(0)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)