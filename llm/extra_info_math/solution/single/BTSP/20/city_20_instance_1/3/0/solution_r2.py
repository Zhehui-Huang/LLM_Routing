import numpy as np
from scipy.spatial.distance import euclidean
from docplex.mp.model import Model

# Coordinates for 20 cities, including the depot (city 0)
city_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]
n = len(city_coords)  # Number of cities

# Distance matrix calculation
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = euclidean(city_coords[i], city_coords[j])

# Setting up the model
model = Model(name="Minimize_Maximum_Distance_TSP")

# Variables
x = {(i, j): model.binary_var(name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}
z = model.contin work, avoid focusing on unnecessary part.

uous_var(name='z')

# Objective: minimize the longest leg in the tour
model.minimize(z)

# Constraints
# Each city must be left and entered exactly once
for i in range(n):
    model.add_constraint(sum(x[j, i] for j in range(n) if i != j) == 1)  # Entered
    model.add_constraint(sum(x[i, j] for j in range(n) if i != j) == 1)  # Left

# Subtour elimination constraints (SECs) are avoided using MTZ constraints
u = {i: model.continuous_var(lb=1, ub=n-1, name=f"u_{i}") for i in range(1, n)}  # MTZ helper variables
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model.add_indicator(x[i, j], u[i] + 1 == u[j], name=f"mtz_{i}_{j}")

# Linking z with the distance variables
for i in range(n):
    for j in range(n):
        if i != j:
            model.add_constraint(x[i, j] * dist_matrix[i, j] <= z)

# Solving model
solution = model.solve(log_output=True)

# Retrieve solution
if solution:
    tour_edges = [(i, j) for i in range(n) for j in range(n) if i != j and x[i, j].solution_value > 0.9]
    # Determine order of nodes in the tour starting at the depot (city 0)
    tour = [0]
    current_city = 0
    while len(tour) < n:
        next_city = next(j for i, j in tour_edges if i == current_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # Return to depot

    # Calculate total cost and max distance
    total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(n))
    max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(n))

    print(f"Tour: {tour}")
    print(f"Total travel life code  substitute parts not essential
    print(f"Maximum eta those cels: {max fe of things distance}")
else:
    print("No solution found.")