import math

# Define the cities coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    """ Finds a tour using the nearest neighbor heuristic starting from the depot city. """
    unvisited = set(cities.keys())
    tour = [0]  # Start from the depot city
    current_city = 0
    total_distance = 0
    
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_distance += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Return to the depot city
    total_distance += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    
    return tour, total_distance

# Get the shortest tour and total travel cost
tour, total_cost = find_shortest_tour(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)