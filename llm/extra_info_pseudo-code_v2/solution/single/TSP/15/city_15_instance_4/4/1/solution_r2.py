import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest possible route using permutations
def find_shortest_path():
    smallest_distance = float('inf')
    best_path = []
    # All cities except the depot
    city_indices = list(cities.keys())[1:]
    
    # Permute through all possible city orders
    for path in permutations(city_indices):
        # Including depot as the start and end of the path
        current_path = [0] + list(path) + [0]
        # Calculate the total distance
        current_distance = sum(distance(current_path[i], current_path[i+1]) for i in range(len(current_path) - 1))
        
        # If the found path has a smaller distance, update the best found
        if current_distance < smallest_distance:
            smallest_distance = current_distance
            best_path = current_path
            
    return best_path, smallest_distance

# Execute the function to get results
tour_result, tour_distance = find_shortest_path()

# Result outputs
tour_result, tour_distance