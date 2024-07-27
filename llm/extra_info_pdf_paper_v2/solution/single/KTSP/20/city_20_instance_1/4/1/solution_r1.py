import math
from itertools import permutations

# Coordinates of each city
cities_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Calculation of Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities_coords[city1]
    x2, y2 = cities_coords[city2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Number of cities including the depot
num_cities = len(cities_coords)

# Getting all subsets of the required size k+1 including the depot
def get_subsets(fullset, size):
    return [subset for subset in permutations(fullset, size) if subset[0] == 0]

# Finding the shortest tour
def find_shortest_tour():
    all_possible_subsets = get_subsets(range(num_cities), 7)
    shortest_distance = float('inf')
    best_tour = []
    
    for subset in all_possible_subsets:
        # Generate all permutations of the current subset to find the shortest tour
        for tour in permutations(subset):
            if tour[0] == 0:  # Ensure it starts at the depot
                # Calculate the total distance of this tour permutation
                total_distance = 0
                for i in range(len(tour) - 1):
                    total_distance += calculate_distance(tour[i], tour[i + 1])
                total_distance += calculate_distance(tour[-1], tour[0])  # return to depot
                
                # Check if this tour is better than what we have already found
                if total_distance < shortest_distance:
                    shortest_distance = total_distance
                    best_tour = tour
    
    return best_tour, shortest_distance

# Execute the function and print the result
best_tour, shortest_distance = find_shortest_tour()
print("Tour:", list(best_tour) + [0])  # Append the return to depot
print("Total travel cost:", shortest_distance)