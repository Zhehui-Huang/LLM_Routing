import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total")
        a, b = tour[i], tour[i+1]
        total_distance += distance_matrix[a][b]
    return total_distance

def find_shortest_tour(coordinates, groups):
    # Calculate distance matrix
    num_cities = len(coordinates)
    distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    # Initial tour setup
    best_tour = [0] + [random.choice(group) for group in groups] + [0]
    best_distance = calculate_total_distance(best_tour, distance_matrix)
    
    # Start the iterated search
    num_iterations = 5000
    for _ in range(num_iterations):
        new_tour = [best_tour[0]]  # start from depot
        for group in groups:
            selectable = list(set(group) - set(new_tour))
            selected = random.choice(selectable)
            new_tour.append(selected)
        new_tour.append(best_tour[0])  # end at depot
        
        new_distance = calculate_total_distance(new_tour, distance_matrix)
        if new_distance < best_distance:
            best_tour, best_distance = new_tour, new_distance
    
    return best_tour, best_distance

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58),
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0),
    (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

# Grouped cities
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Find the shortest tour
tour, total_cost = find_shortest_tour(coordinates, groups)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")