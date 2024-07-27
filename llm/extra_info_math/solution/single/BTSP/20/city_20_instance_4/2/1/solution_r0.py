import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY

# City coordinates indexed from 0 to 19
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

n = 20  # Number of cities including the depot (1 depot + 19 other cities)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distances matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create model
model = Model(sense=minimize)

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]  # auxiliary variables for subtour elimination
z = model.add_var()  # variable to minimize

# Objective: minimize the maximum edge used in the solution
model.objective = z

# Constraints
# Every city is connected with some other city
for i in range(1, n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1

# Every city is reached from some other city
for j in range(1, n):
    model += xsum(x[i][j] for i in range(n) if i != j) == 1

# Eliminate subtours and set the Z variable correctly
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + 1 <= (n - 1) * (1 - x[i][j])
            model += z >= distances[i][j] * x[i][j]

# Departing and returning to the depot constraints
model += xsum(x[0][j] for j in range(1, n)) == 1
model += xsum(x[i][0] for i in range(1, n)) == 1

# Solve model
model.optimize()

# Extract solution
tour = []
if model.num_solutions:
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))

# Make tour order explicit
order = []
current_location = 0
while True:
    for (i, j) in tour:
        if i == current_location:
            order.append(i)
            tour.remove((i, j))
            current_location = j
            break
    if current_location == 0:
        break

order.append(0)  # return to depot

# Calculate total travel cost and maximum distance
total_travel_cost = sum(distances[order[i]][order[i+1]] for i in range(len(order) - 1))
max_distance = max(distances[order[i]][order[i+1]] for i in range(len(order) - 1))

print(f"Tour: {order}")
print(f"Total travel cost: {total_travel_add_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")