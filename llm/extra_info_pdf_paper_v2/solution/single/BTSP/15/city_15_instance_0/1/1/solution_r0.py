import numpy as np

# Coordinates for the cities including the depot
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Compute Euclidean distance between two points
def calc_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create a distance matrix
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = calc_distance(coordinates[i], coordinates[j])

# Import the necessary TSP solver
from scipy.optimize import linear_sum_assignment

# Create a cost matrix for the assignment problem
cost_matrix = np.zeros((num_cities * 2, num_cities * 2))

# Mapping between single trip distance matrix and cost matrix for assignment problem
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[i][j + num_cities] = dist_matrix[i][j]

# Solve the assignment problem (minimum cost perfect matching)
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Extracting the tour from the assignment
matching = col_ind[:num_cities] - num_cities
tour = [0]  # start at the depot city
visited = [False] * num_cities
current = 0
visited[0] = True

# Create tour from matching (simple heuristic approach)
while len(tour) < num_cities:
    next_city = matching[current]
    if not visited[next_city]:
        tour.append(next_city)
        visited[next_city] = True
        current = next_city

# Closing the tour by returning to the depot
tour.append(0)

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    city1, city2 = tour[i], tour[i + 1]
    distance = dist_matrix[city1][city2]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")