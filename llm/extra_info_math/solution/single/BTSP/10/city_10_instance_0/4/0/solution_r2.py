import math
import pulp

# Coordinates of cities including the depot city 0
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), 
    (51, 69), (47, 39), (62, 26), (79, 31), 
    (61, 90), (42, 49)
]

n = len(coordinates)  # Number of coordinates (including depot)

# Distance calculation function
def euclidean(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a dictionary to hold distances
distances = {
    (i, j): euclidean(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Create the optimization problem
model = pulp.LpProblem("Minimize_MaxEdge_TSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if the path i to j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
# Continuous variable to minimize: the largest distance travelled between any two cities in the solution
z = pulp.LpVariable("z", lowBound=0)

# Objective: Minimize the maximum edge length in the tour
model += z

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave each city only once
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination: Miller-Tucker-Zemlin formulation (u variable adds order to the cities)
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Ensure that the max distance variable 'z' is indeed the largest distance used
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[(i, j)] * x[(i, j)] <= z

# Solve the model
model.solve()

# Extract the solution
tour = []
current_location = 0
while True:
    next_location = next(j for j in range(n) if j != current_location and pulp.value(x[(current_location, j)]) == 1)
    tour.append(current_location)
    if next_location == 0:  # If we are back to the depot location
        break
    current_location = next_location
    
tour.append(0)  # Complete the loop back to depot

# Calculate maximum and total distance using the tour
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")