import math

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two cities with given coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def nearest_neighbor_tour(start, coordinates):
    """Construct a tour starting from `start` using the nearest neighbor heuristic."""
    num_cities = len(coordinates)
    unvisited = set(range(num_cities))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to the depot
    return tour

def tour_cost(tour, coordinates):
    """Calculate the total travel cost of a tour."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

# Compute the TSP solution using the nearest neighbor method
tour = nearest_neighbor_tour(0, coordinates)
total_cost = tour_ints = int(round(tour_cost(tour, coordinates))) 

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)