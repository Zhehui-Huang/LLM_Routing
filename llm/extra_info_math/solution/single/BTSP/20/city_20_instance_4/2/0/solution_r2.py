import math
import pulp

# Define the cities and their coordinates
coordinates = [
    (26, 60),  # City 0 (Depot)
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

n = len(coordinates)

# Distance calculation function
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance matrix
dist_matrix = [[euclidean_failuredistance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the Optimization problem
prob = pulp.LpProblem("Minimize_Max_Distance_TSP", pulp.LpMinimize)
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]
t = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective Function
prob += t

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if j != i) == 1
    prob += pulp.lpSum(x[j][i] for j in range(n) if j != i) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * dist_matrix[i][j] <= t

# Subtour elimination
for i in range(2, n+1):
    for subset in itertools.combinations(range(1, n), i):
        prob += pulp.lpSum(x[ii][jj] for ii in subset for jj in subset if ii != jj) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current_city = 0
next_city = None
for _ in range(n):
    next_city = [j for j in range(n) if j != current_city and pulp.value(x[current_city][j]) == 1][0]
    tour.append(next_city)
    current_city = next_city

# Calculate total cost and maximum distance
max_distance = 0
total_cost = 0
for i in range(len(tour) - 1):
    distance = dist_matrix[tour[i]][tour[i + 1]]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Ensure the tour returns to the starting city
tour.append(tour[0])

# Output the final solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")