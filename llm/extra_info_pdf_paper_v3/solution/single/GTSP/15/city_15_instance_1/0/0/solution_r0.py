import itertools
import math

# Coordinates of the cities, indexed by city number
coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Groups of cities
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Function to calculate the total tour distance
def calculate_tour_distance(tour):
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Find the shortest path that visits one city from each group plus the depot
def find_shortest_tour():
    shortest_distance = float('inf')
    best_tour = None
    
    # Generate all combinations of cities taking one from each group
    for combination in itertools.product(*city_groups):
        current_tour = [0] + list(combination) + [0]  # Start and end at depot
        current_distance = calculate_tour_distance(current_tour)
        
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_tour = current_tour

    return best_tour, shortest_distance

# Execute the function
tour, total_distance = find_shortest_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")