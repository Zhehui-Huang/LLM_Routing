import pulp
import math

# Define the cities and their locations
locations = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
             (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

n = len(locations)  # Number of cities including the depot

# Calculate the Euclidean distance between every pair of nodes
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

distances = {(i, j): euclidean_distance(locations[i], locations[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decide if we travel between two nodes
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective Function: Minimize the sum of distances of the travel path
prob += pulp.lpSum([distances[(i, j)] * x[(i, j)] for i in range(n) for j in range(n) if i != j])

# Constraints
# Every city has exactly one outgoing connection
for i in range(n):
    prob += pulp.lpSum([x[(i, j)] for j in range(n) if (i, j) in x]) == 1

# Every city has exactly one incoming connection
for j in range(n):
    prob += pulp.lpSum([x[(i, j)] for i in range(n) if (i, j) in x]) == 1

# Avoid sub-tour formation; each subset of nodes must not be disconnected
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour from the solved problem
tour = [0]
total_cost = 0
while len(tour) < n:
    i = tour[-1]
    next_city = [j for j in range(n) if j != i and (i, j) in x and pulp.value(x[(i, j)]) == 1][0]
    tour.append(next_city)
    total_cost += distances[(i, next_city)]

# Adding the return to the depot
total_cost += distances[(tour[-1], 0)]
tour.append(0)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")