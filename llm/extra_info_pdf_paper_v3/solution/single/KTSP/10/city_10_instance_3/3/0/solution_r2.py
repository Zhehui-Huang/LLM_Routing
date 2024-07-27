import itertools
from math import sqrt

# Define the city coordinates
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

# Distance calculation helper function using Euclidean distance
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute all possible combinations of 6 cities initiating and concluding the tour at the depot city
# The depot city is 0, and we want to visit a total of 7 cities (that includes the depot city).
city_combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)

# Variables to hold the best (shortest) tour and its distance
shortest_tour = None
shortest_distance = float('inf')

# Check all combinations
for combination in city_combinations:
    all_tours = itertools.permutations(combination)
    # Adding depot city at start and end (city 0)
    for tour in all_tours:
        complete_tour = [0] + list(tour) + [0]
        # Calculate total distance for the tour
        tour_distance = sum(euclidean_distance(complete_tour[i], complete_tour[i+1]) for i in range(len(complete_tour) - 1))
        # Update shortest found
        if tour_distance < shortest_distance:
            shortest_distance = tour_distance
            shortest_tour = complete_tour

# Print the final outputs
print("Tour:", shortest_tour)
print("Total travel cost:", round(shortest_distance, 2))