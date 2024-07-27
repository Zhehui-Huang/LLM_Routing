import math
import random

# City coordinates with depot at index 0
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize a random tour
def initial_tour():
    tour = [0]  # start at the depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # end at the depot
    return tour

# Calculate total distance of a tour
def total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += calculate_distance(tour[i], tour[i+1])
    return total_dist

# Simple local search heuristic: Swap within groups to find better route
def local_search(tour):
    best_tour = tour[:]
    min_dist = total_distance(tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if tour[i] in groups[j-1] and tour[j] in groups[i-1]:
                    # Attempt to swap cities
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_dist = total_distance(new_tour)
                    if new_dist < min_dist:
                        best_tour = new_tour[:]
                        min_dist = new_dist
                        improved = True
    return best_tour

# Find the optimal route
initial_tour = initial_tour()
optimized_tour = local_search(initial_tour)
optimized_distance = total_distance(optimized_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance:.2f}")