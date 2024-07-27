import math
import pulp

# Step 1: Define the cities and their coordinates
coordinates = [
    (26, 60),  # City 0
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

# Step 2: Create a distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Step 3: Integer programming optimization
prob = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)
t = pulp.LpVariable("max_consecutive_distance", lowBound=0, cat='Continuous')

# Objective function
prob += t

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1
    
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * distances[i][j] <= t

# Subtour elimination via Miller-Tucker-Zemlin conditions
u = pulp.LpVariable.dicts('u', range(n), 0, n-1, pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i][j] <= n - 1

# Solve the problem
prob.solve()

# Extract the tour from the solution
path = []
current_city = 0
visited = [False] * n
count = 0
while count < n:
    for j in range(n):
        if pulp.value(x[current_city][j]) == 1:
            visited[current_city] = True
            path.append(current_city)
            current_city = j
            count += 1
            break
path.append(0)  # Return to the depot city

# Calculate the total cost and maximum distance
max_distance = 0
total_cost = 0
for i in range(len(path)-1):
    d = distances[path[i]][path[i+1]]
    total_cost += d
    if d > max_distance:
        max_usual_distance = d

# Output results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_usual_distance:.2f}")