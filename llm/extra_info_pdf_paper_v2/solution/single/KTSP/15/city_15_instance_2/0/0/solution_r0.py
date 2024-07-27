import math
import itertools

def euclidean_distance(c1, c2):
    # Calculating Euclidean distance between two cities
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_tour_cost(tour, distance_matrix):
    # Calculating the total travel distance of a given tour
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# City coordinates
coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Create a distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in coordinates] for i in coordinates]

# Select 7 additional cities to visit
# Simple heuristic: choose cities closest to the depot city 0, excluding city 0
distances_from_depot = sorted((distance_matrix[0][i], i) for i in range(1, 15))
selected_cities = [0] + [x[1] for x in distances_from_depot[:7]]

#find the shortest possible tour visiting these cities
# Simple approach: use permutations and select the minimum distance tour
all_possible_tours = itertools.permutations(selected_cities + [0])
shortest_tour = min(all_possible_tours, key=lambda tour: total_tour_cost(tour, distance_matrix))
shortest_distance = total_tour_cost(shortest_tour, distance_matrix)

# Output the results
print("Tour:", list(shortest_tour))
print("Total travel cost:", shortest_distance)