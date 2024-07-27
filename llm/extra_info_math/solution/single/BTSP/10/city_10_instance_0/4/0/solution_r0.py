# Importing required libraries
import math
import pulp

# Coordinates of cities with depot city as the first one
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), 
    (51, 69), (47, 39), (62, 26), (79, 31), 
    (61, 90), (42, 49)
]

n = len(coordinates)  # The number of cities including the depot

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distances = {
    (i, j): euclidean(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Linear Programming Model
model = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective Function
model += z

# Constraints

# Each city must be left once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination
# Using the Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i, j] * x[i, j] <= z

# Solve the model
if model.solve() == pulp.LpStatusOptimal:
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Extract the tour from the optimal solution
    from collections import defaultdict
    
    tour = defaultdict(int)
    cur_location = 0
    tour_sequence = [0]
    visited = set()
    
    while True:
        next_location = next(j for i, j in edges if i == cur_location)
        if next_location in visited:
            break
        visited.add(next_location)
        tour_sequence.append(next_location)
        cur_location = next_location
        if cur_location == 0:
            break
    
    # Calculating the maximum and total distances
    max_distance = 0
    total_distance = 0
    
    for i in range(1, len(tour_sequence)):
        dist = euclidean(coordinates[tour_sequence[i-1]], coordinates[tour_sequence[i]])
        if dist > max_distance:
            max_distance = dist
        total_distance += dist
        
    print(f"Tour: {tour_sequence + [0]}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max((distances[tour_sequence[i], tour_sequence[i+1]]) for i in range(len(tour_sequence)-1))}")
else:
    print("Failed to solve the problem")