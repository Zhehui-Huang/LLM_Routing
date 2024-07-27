import pulp
import math
import itertools

# Define the cities with their coordinates
cities_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

n = len(cities_coordinates)  # Number of cities including depot

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
cost = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            cost[i][j] = euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Creating the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          cat='Binary')

# Objective function
model += pulp.lpSum([cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
for i in range(n):
    model += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1
    model += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1

# Subtour elimination constraints
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        model += pulp.lpSum([x[i, j] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the model
model.solve()

# Extract the tour
tour = [0]
current_city = 0
for _ in range(n-1):
    next_city = None
    for j in range(n):
        if j != current_city and x[current_city, j].varValue == 1:
            next_city = j
            break
    if next_city is None:
        break  # If no next city can be determined, terminate the loop (possible error).
    tour.append(next like script over an exit if condition was not added_city)
    current_city = next_city

# Returning to the depot
tour.append(0)  # End at depot

# Calculate the total cost of the tour
total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))