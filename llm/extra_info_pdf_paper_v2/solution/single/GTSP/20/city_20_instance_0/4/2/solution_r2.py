import math

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Grouping of cities
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the shortest possible route that visits one city from each group and returns to the start
def find_optimal_path():
    min_total_distance = float('inf')  # Using infinity as initial comparison value
    best_tour = None
    
    # Generate all combinations of selecting one city from each group
    from itertools import product
    for combination in product(groups[0], groups[1], groups[2]):
        # Create the full round trip tour starting and ending at the depot
        tour = [0] + list(combination) + [0]
        
        # Calculate the total distance of this potential tour
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += euclidean_distance(tour[i], tour[i + 1])
        
        # Update the minimum distance and corresponding tour if current one is better
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_tour = tour
    
    return best_tour, min_total_distance

# Calculate and print the optimal tour and its total cost
optimal_tour, optimal_distance = find_optimal_path()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_distance)