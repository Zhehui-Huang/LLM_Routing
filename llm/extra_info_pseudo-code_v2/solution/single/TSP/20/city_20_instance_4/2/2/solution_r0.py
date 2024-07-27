import numpy as np

# Coordinates for each city including the depot
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(a, b):
    return np.sqrt((coordinates[b][0] - coordinates[a][0]) ** 2 + (coordinates[b][1] - coordinates[a][1]) ** 2)

# Number of cities
num_cities = len(coordinates)

# Calculate all distances between cities
dist_matrix = np.array([[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Function to find the shortest tour using a greedy nearest neighbor approach initiated from the depot
def find_tour():
    unvisited = set(range(1, num_cities))  # all cities except the depot
    tour = [0]  # start at depot
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current, x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the depot
    return tour

# Calculate the tour
tour = find_tour()

# Calculate the total travel cost of the tour
total_travel_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")