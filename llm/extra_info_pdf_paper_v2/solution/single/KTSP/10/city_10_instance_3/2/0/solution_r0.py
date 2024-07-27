import itertools
import math
from scipy.spatial import distance

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Define the cities with their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Define the number of cities the robot has to visit including the depot
k = 7

# Selecting the best tour using a combination and permutation strategy
def find_best_tour():
    all_tours = []
    for subset in itertools.combinations([key for key in cities if key != 0], k - 1):
        # Include the depot
        subset = (0, *subset)
        
        # Find all permutations of the subset to find the best tour
        for perm in itertools.permutations(subset):
            # Ensuring the tour starts and ends at the depot
            if perm[0] == 0:
                tour_distance = sum(euclidean_distance(cities[perm[i]], cities[perm[i + 1]]) for i in range(len(perm) - 1))
                tour_distance += euclidean_distance(cities[perm[-1]], cities[0])  # To return to the depot
                all_tours.append((perm + (0,), tour_distance))

    # Find the tour with the minimum distance
    best_tour = min(all_tours, key=lambda x: x[1])
    return best_tour

# Calculate the best tour
best_tour = find_best_tour()
print("Tour:", list(best_tour[0]))
print("Total travel cost:", best_tour[1])