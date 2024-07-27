import itertools
import math
from sys import maxsize

# Cities with their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate total distance of a tour
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Choosing the best tour among sample tours of exactly 7 cities starting/ending at depot city 0
def find_best_tour():
    min_distance = maxsize
    best_tour = None
    
    # Generate all combinations of 6 additional cities to visit, since the robot starts and stops at city 0
    for city_combination in itertools.combinations(range(1, 20), 6):
        # Include city 0 as the start and end point
        full_tour = [0] + list(city_combination) + [0]
        # Generate all permutations of the inner cities
        for permuted_combination in itertools.permutations(city_combination):
            permuted_tour = [0] + list(permuted_combination) + [0]
            distance = calculate_tour_distance(permuted_tour)
            
            if distance < min_distance:
                min_distance = distance
                best_tour = permuted_tour
                
    return best_tour, min_distance

# Main execution
best_tour, min_distance = find_best_tour()

# Output
print("Tour:", best_tour)
print("Total travel cost:", min_distance)