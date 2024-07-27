import math
from itertools import permutations

# Define a function to calculate the Euclidean distance between two points
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# List of city coordinates
city_coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to compute the total distance of a tour
def tour_dist(tour):
    dist = 0
    for i in range(len(tour) - 1):
        dist += calc_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return dist

# Find the shortest tour of 8 cities, including the depot
def shortest_tour():
    min_dist = float('inf')
    best_tour = None

    # Generate all subsets of 7 other cities (excluding the depot)
    for subset in permutations([k for k in city_coords if k != 0], 7):
        # Create the tour starting and ending at the depot
        current_tour = [0] + list(subset) + [0]
        current_dist = tour_dist(current_tour)
        # Update the minimum tour if the current one is shorter
        if current_dist < min_dist:
            min_dist = current_dist
            best_tour = current_tour

    return best_tour, min_dist

# Calculate the shortest tour
best_tour, best_tour_distance = shortest_tour()

# Print out the results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_distance)