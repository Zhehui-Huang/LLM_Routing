import numpy as np
from scipy.spatial.distance import euclidean
from docplex.mp.model import Model

# Define the coordinates of the cities
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

n = len(city_coords)

# Compute the distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = euclidean(city_coords[i], city_coords[j])

# Create model
model = Model(name="Minimize_Maximum_Distance_TSP")

# Create variables
x = {(i, j): model.binary_var(name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}
z = model.continuous_var(name='z', lb=0)

# Objective: minimize the maximum distance
model.minimize(z)

# Constraints
# Every city must be entered and left exactly once
for i in range(n):
    model.add_constraint(model.sum(x[i, j] for j in range(n) if i != j) == 1, ctname=f"leave_{i}")
    model.add_constraint(model.sum(x[j, i] for j in range(n) if i != j) == 1, ctname=f"enter_{i}")

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model.add_constraint(x[i, j] * dist_matrix[i, j] <= z)

# Subtour Elimination Constraints - using the lazy constraints approach within solve process

# Define a function for generating subtour constraints dynamically
def subtour_callback(model, where):
    if where == model.cb.lazy:
        x_sol = model.cb.get_solution(x)
        tours = extract_tours(x_sol)
        for tour in tours:
            if len(tour) != n:
                model.cb.lazy(model.sum(x[i, j] for i in tour for j in tour if i != j) <= len(tour) - 1)

# Solve model and implement subtour callback
model.parameters.mip.tolerances.mipgap = 0   # Set to zero for exact integer solutions
model.solve(log_output=True, clean_before_solve=True, callback=subtour_callback)

# Extract solution
optimal_tour = extract_tours({(i, j): x[i, j].solution_value for i in range(n) for j in range(n) if i != j})[0]
optimal_tour.append(optimal_tour[0])  # Returning to the starting city

# Calculate the total travel cost and maximum distance in the optimal tour
total_cost = sum(dist_matrix[optimal_tour[i], optimal_tour[i + 1]] for i in range(len(optimal_tour) - 1))
max_distance = max(dist_matrix[optimal_tour[i], optimal_tour[i + 1]] for i in range(len(optimal_tour) - 1))

# Function to extract tours
def extract_tours(solution):
    visited = set()
    tours = []
    for start in range(n):
        if start not in visited:
            tour = [start]
            while True:
                visited.add(tour[-1])
                next_city = next(i for i in range(n) if solution.get((tour[-1], i), 0) > 0.5)
                if next_city in tour:
                    tour.append(next_city)
                    break
                tour.append(next_city)
            tours.append(tour)
    return tours


print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")