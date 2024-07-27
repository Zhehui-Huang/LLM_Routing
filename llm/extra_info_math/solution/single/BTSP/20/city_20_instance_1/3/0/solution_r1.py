import numpy as np
from scipy.spatial.distance import euclidean
from math import floor
from docplex.mp.model import Model

# City coordinates
city_coords = [
    (14, 77),   # Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]
n = len(city_coords)  # number of cities

# Distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = euclidean(city_coords[i], city_coords[j])

# Create model
model = Model(name="Minimize_Maximum_Distance_TSP")

# Variables
x = {(i, j): model.binary_var(name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}
z = model.continuous_var(name='z')

# Objective
model.minimize(z)

# Constraints
for i in range(n):
    model.add_constraint(sum(x[i, j] for j in range(n) if i != j) == 1)
    model.add_constraint(sum(x[j, i] for j in range(n) if i != j) == 1)

# Maximum distance constraint for edges
for i in range(n):
    for j in range(n):
        if i != j:
            model.add_constraint(dist_matrix[i, j] * x[i, j] <= z)

# Solve model
solution = model.solve(log_output=True)

def find_tours():
    """ Function to extract tours from the solution """
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j and x[i, j].solution_value > 0.9]
    tours = []
    while arcs:
        start_arc = arcs[0]
        current_tour = [start_arc]
        arcs.remove(start_arc)
        last_city = start_arc[1]
        while last_city != current_tour[0][0]:
            next_arc = next(arc for arc in arcs if arc[0] == last_city)
            current_tour.append(next_arc)
            arcs.remove(next_arc)
            last_city = next_arc[1]
        tours.append(current_tour)
    return tours

tours = find_tours()[0]  # Assume one tour (since depot returns)
optimal_tour = [t[0] for t in tours] + [tours[0][0]]

# Calculate results
max_distance = max(dist_matrix[optimal_tour[i], optimal_tour[i + 1]] for i in range(n))
total_cost = sum(dist_matrix[optimal_tour[i], optimal_tour[i + 1]] for i in range(n))

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")