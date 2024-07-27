import pulp
import math

# Define the cities and the coordinates
city_coordinates = [
    (50, 42), # Depot city 0
    (41, 1),  # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49)  # City 9
]

n = len(city_coordinates)

# Calculate costs as Euclidean distances
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

c = [[calc_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective Function
model += pulp.lpSum(c[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):
        model += pulp.lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Extract the tour and calculate total cost
tour = []
current_city = 0
total_cost = 0

while True:
    for j in range(n):
        if pulp.value(x[current_city][j]) == 1:
            tour.append(current_city)
            total_cost += c[current_city][j]
            current_city = j
            break
    if current_city == 0:
        break

tour.append(0)  # Complete the tour by returning to the depot

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)