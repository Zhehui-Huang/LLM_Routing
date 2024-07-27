import pulp
import math

# Define the city coordinates:
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Define the groups:
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate distances:
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


size = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(size)] for i in range(size)]

# Create the LP problem:
prob = pulp.LpProblem("RobotTour", pulp.LpMinimize)

# Create variables:
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(size) for j in range(size)], cat='Binary')

# Objective function:
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(size) for j in range(size))

# Constraints:
# Each group must connect exactly once to another city:
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(size) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(size) if j not in group) == 1

# Continuous variable to eliminate subtours:
u = pulp.LpVariable.dicts('u', range(1, size), lowBound=0, cat='Continuous')

# Subtour elimination and flow conservation:
for i in range(1, size):
    for j in range(1, size):
        if i != j:
            prob += u[i] - u[j] + (size - 1) * x[i, j] <= size - 2

# Solve the problem
prob.solve()

# Extract the solution:
tour = []
current_city = 0
visited = set([current_city])
while True:
    for next_city in range(size):
        if pulp.value(x[current_city, next_city]) == 1:
            tour.append(current_city)
            current_city = next_city
            visited.add(next_city)
            break
    if current_city == 0:
        break
tour.append(0)  # End at the starting city

# Calculate the total cost:
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output:
print("Tour:", tour)
print("Total travel cost:", total_cost)