import math

# Given coordinates for each city, including the depot city at index 0
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56), 
    (85, 71),
    (6, 76)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def find_shortest_tour(coords):
    """ Find the shortest tour using the nearest neighbor heuristic. """
    n = len(coords)
    unvisited = list(range(1, n))  # Start with every city except the depot city 0 included in unvisited list
    tour = [0]  # Tour starts at depot city
    current_city = 0
    
    # Visit next the nearest unvisited city until all cities are visited
    while unvisited:
        nearest = min(unvisited, key=lambda city: euclidean_distance(coords[current_city], coords[city]))
        tour.append(nearest)
        current_city = nearest
        unvisited.remove(nearest)
    
    tour.append(0)  # Return to the depot at the end of the tour
    
    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coords[tour[i-1]], coords[tour[i]])
    
    return tour, total_cost

# Calculate the tour and total travel cost
tour, total_cost = find_shortest_tour(coordinates)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")