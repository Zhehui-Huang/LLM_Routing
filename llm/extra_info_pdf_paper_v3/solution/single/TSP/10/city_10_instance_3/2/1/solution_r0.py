import math

# City coordinates
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

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def nearest_neighbor_tsp(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited:
        nearest_city, min_distance = None, float('inf')
        
        for city in unvisited:
            distance = euclidean_distance(current_city, city)
            if distance < min_distance:
                nearest_city = city
                min_distance = distance
        
        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the start city
    return_distance = euclidean_distance(tour[-1], start_city)
    total_cost += return_distance
    tour.append(start_city)

    return tour, total_cost

# Compute the TSP tour starting from the depot city 0
tour, total_cost = nearest_neighbor_tsp(0)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)