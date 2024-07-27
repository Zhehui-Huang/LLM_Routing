import pulp
import math
from itertools import combinations

# Define the cities' coordinates
coordinates = [
    (26, 60),  # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1),
    (71, 73), (82, 47), (19, 25), (75, 9), 
    (52, 54), (64, 72), (14, 89)
]

# Number of cities (including depot)
n = len(coordinates)

# Distance computation function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Construct distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Create the ILP problem
problem = pulp.LpProblem("Minimize_Maximum_Distance_TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if path i to j is taken, 0 otherwise
x = pulp.LpVariable.dicts("x", distance_matrix.keys(), cat=pulp.LpBinary)

# Maximum distance variable
D = pulp.LpVariable("D", lowBound=0, cat=pulp.LpContinuous)

# Objective: minimize the maximum distance D
problem += D

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if j != i) == 1  # Leave each city once
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if j != i) == 1  # Enter each city once
    
# Constrain D to be greater than or equal to each x_ij * distance
for i, j in distance_matrix.keys():
    problem += D >= x[(i, j)] * distance_matrix[(i, j)]

# Subtour elimination constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):  # 1 to n-1, ignoring the depot
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the ILP problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Check if a valid solution was found
if pulp.LpStatus[status] == 'Optimal':
    # Extract the tour from the decision variables
    tour = []
    current_city = 0
    steps = 0
    
    while steps < n:
        for next_city in range(n):
            if current_city != next_city and pulp.value(x[current_city, next_city]) == 1:
                tour.append(next_city)
                current_city = next_city
                steps += 1
                break
    tour.append(0)  # Make sure to return to the depot
    
    # Compute the total and maximum distances using the tour
    total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No optimal solution was found.")