import math

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def find_tour(cities):
    """ Find a tour that starts and ends at the depot (city 0) based on the nearest neighbor heuristic. """
    unvisited = set(cities.keys())
    tour = [0]
    current_city = 0
    total_cost = 0
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to the depot
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    
    return tour, total_cost

# Compute the shortest tour and total travel cost using the nearest neighbor heuristic.
tour, total_cost = find_tur(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total.cost)