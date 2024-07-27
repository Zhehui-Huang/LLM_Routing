import math
from itertools import permutations

# City coordinates including the depot city (index 0)
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour):
    """ Calculate the total distance of the tour including return to the starting city. """
    return sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Generate permutations of city indices, exclude the depot city 0
def find_best_tour():
    num_cities = len(city_coordinates)
    best_distance = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, num_cities)):
        current_tour = [0] + list(perm) + [0]
        current_distance = total_distance(current_tour)
        if current_distance < best_distance:
            best_tour = current_tour
            best_distance = current_distance
    
    return best_tour, best_distance

# Find the best tour using the given coordinate data
best_tour, best_tour_distance = find_best_tour()

# Print results
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_distance, 2))