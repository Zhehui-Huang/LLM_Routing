import math
import itertools

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_and_max_distance(tour, cities):
    """Calculates the total and maximum distance of a given tour based on city coordinates."""
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    # Return to the start city
    dist = euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_distance += dist
    if dist > max_distance:
        max_distance = dist
    return total_distance, max_distance

def find_optimal_tour(cities):
    """ Attempts to find an optimal tour minimizing the maximum distance between consecutive cities."""
    n = len(cities)
    best_tour = list(range(n))
    # Shuffle tour back to start with depot
    best_tour.append(0)
    best_total, best_max = calculate_total_and_max_distance(best_tour, cities)

    # Iterate over all possible tours to find the optimal one, this is feasible for small n (<11)
    for perm in itertools.permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        total_dist, max_dist = calculate_total_and_max_distance(current_tour, cities)
        # Update the best tour if found a new optimal one by max distance criteria
        if max_dist < best_max or (max_dist == best_max and total_dist < best_total):
            best_tour, best_total, best_max = current_tour, total_dist, max_dist

    return best_tour, best_total, best_max

# Calculate the best tour
optimal_tour, total_travel_cost, max_consecutive_distance = find_optimal_tour(cities)

print("Tour:", optimal_tour)
print("Total travel cost:", total_travel_cat)
print("Maximum distance between consecutive cities:", max_consecutive_distance)