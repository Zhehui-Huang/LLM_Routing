import math

# List of cities indices and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49),
    14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18:(51, 58),
    19:(30, 48)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def nearest_neighbor_tour(start, cities):
    """ Construct a tour using the nearest neighbor strategy, starting from a given city. """
    unvisited = list(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to the start
    return tour

# Construct a tour with nearest neighbor and monitor max distance
def max_minimized_tour(start, cities):
    tour = nearest_neighbor_tour(start, cities)
    max_distance = 0
    total_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    
    return tour, total_distance, max_distance

# Calculate the tour, total travel cost and maximum distance
calculated_tour, total_cost, max_consecutive_distance = max_minimized_tour(0, cities)

print(f"Tour: {calculated_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")