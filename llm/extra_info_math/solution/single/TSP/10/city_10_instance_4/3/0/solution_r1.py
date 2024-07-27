import pulp
import math
import itertools

# City coordinates as (x, y)
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

num_cities = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Each city is arrived at from exactly one other city
for j in range(num_cities):
    prob += sum(x[i, j] for i in range(num_cities) if i != j) == 1

# Each city is departed to exactly one other city
for i in range(num_cities):
    prob += sum(x[i, j] for j in range(num_cities) if i != j) == 1

# Subtour Elimination Constraints
for s in range(2, num_cities):
    for S in itertools.combinations(range(1, num_cities), s):
        prob += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem using the solver
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour from the variables
tour = [0]
current_city = 0
while len(tour) < num_cities:
    next_cities = [j for j in range(num_cities) if j != current_city and pulp.value(x[current_city, j]) == 1]
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Include the depot city at the end
tour.append(0)

# Calculate the total cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Display the tour and total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")