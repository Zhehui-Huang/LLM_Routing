import numpy as np
from itertools import permutations

# Define the city coordinates
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all pairs distance matrix
num_cities = len(coords)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])

# Function to find the shortest tour
def find_shortest_tour(selected_cities):
    all_tours = permutations(selected_cities)
    min_distance = float('inf')
    best_tour = None
    for tour in all_tours:
        # Calculate the tour distance including return to start
        distance = dist_matrix[tour[-1]][tour[0]]
        for i in range(len(tour) - 1):
            distance += dist_matrix[tour[i]][tour[i + 1]]
        
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    
    return list(best_tour) + [best_tour[0]], min_distance

# Select 15 cities randomly excluding the depot and include the depot city
selected_cities = [0] + random.sample(range(1, num_cities), 15)

# Find the shortest tour for the selected cities
final_tour, total_cost = find_shortest_tour(selected_cities)

print("Tour:", final_tour)
print("Total travel cost:", total_cost)