import numpy as np

# Coordinates of each city, including the depot
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic to find a short path
def find_path(distance_matrix):
    n = len(distance_matrix)
    path = [0]  # Start at the depot city 0
    available_cities = set(range(1, n))
    
    while available_cities:
        last = path[-1]
        next_city = min(available_cities, key=lambda x: distance_matrix[last][x])
        path.append(next_city)
        available_cities.remove(next_city)
    
    path.append(0)  # Return to the depot
    return path

# Get the path
path = find_path(distance_matrix)

# Calculate total distance and maximum distance between consecutive cities
total_distance = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
max_distance = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1))

# Output results
print(f"Tour: {path}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")