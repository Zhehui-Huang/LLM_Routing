import math

# Coordinates of the depot and the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def nearest_neighbor_tour(start_city, cities):
    """Compute the travel path based on the nearest neighbor heuristic."""
    unvisited = set(cities.keys())
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        current_city = nearest_city
        unvisited.remove(current_city)

    tour.append(start_city) # returning to the depot city
    return tour

def calculate_total_distance(tour, cities):
    """Compute the total Euclidean distance for the given tour."""
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return total_distance

# Calculate the tour using nearest neighbor heuristic
tour = nearest_neighbor_tour(0, cities)

# Calculate the total distance of the tour
total_distance = calculate_total_distance(tour, cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")