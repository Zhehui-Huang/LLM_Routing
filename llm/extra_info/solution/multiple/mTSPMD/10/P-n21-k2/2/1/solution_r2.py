import numpy as np
from scipy.spatial.distance import cdist
from mip import Model, xsum, BINARY, INTEGER

# Coordinates of cities including depots
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of cities
num_cities = coordinates.shape[0]

# Distance matrix
distance_matrix = cdist(coordinates, coordinates)

# Set up the model
model = Model()

# Variables
x = [[[model.add_var(var_type=BINARY) for k in range(2)] for j in range(num_cities)] for i in range(num_cities)]
u = [[model.add_var(var_type=INTEGER, lb=0) for i in range(num_cities)] for k in range(2)]

# Objective to minimize the total travel distance
model += xsum(distance_matrix[i][j] * x[i][j][k] for k in range(2) for i in range(num_cities) for j in range(num_cities))

# Constraints
for k in range(2):
    depot = k   # Robot k starts at depot k (0 or 1)
    # Each city must be left and entered only once per vehicle
    for i in range(num_cities):
        model += xsum(x[i][j][k] for j in range(num_cities) if j != i) == 1
        model += xsum(x[j][i][k] for j in range(num_cities) if j != i) == 1

    # Subtour elimination
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                model += u[k][i] - u[k][j] + num_cities * x[i][j][k] <= num_cities - 1
    
# Remaining cities visited exactly once by any vehicle
for i in range(2, num_cities):
    model += xsum(x[j][i][k] for k in range(2) for j in range(num_cities) if j != i) == 1

# Solve the model
model.optimize(max_seconds=300)

# Retrieve the solution
tours = [[], []]

for k in range(2):
    for i in range(num_cities):
        for j in range(num_cities):
            if x[i][j][k].x >= 0.99:
                tours[k].append((i, j))

# Convert the list of edges in the tours to a more readable format
tour_lists = []
for k in range(2):
    tour = []
    if tours[k]:
        # Start from the depot
        current_location = k
        for _ in range(num_cities):
            tour.append(current_location)
            next_moves = [j for i, j in tours[k] if i == current_location]
            if not next_moves:
                break
            current_location = next_moves[0]
            tours[k] = [(i, j) for i, j in tours[k] if i != tour[-1]]
        tour.append(current_location)  # Return to the depot
    tour_lists.append(tour)

# Calculate the cost of each tour
costs = []
for tour in tour_lists:
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    costs.append(cost)

# Output results
for i, (tour, cost) in enumerate(zip(tour_lists, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {sum(costs)}")