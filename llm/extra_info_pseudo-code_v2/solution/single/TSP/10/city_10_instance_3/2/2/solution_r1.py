import math

# Cities' coordinates
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

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def nearest_neighbor_tour(start_city, cities):
    """Generate an initial tour using Nearest Neighbor heuristic."""
    unvisited_cities = list(cities.keys())
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # return to the depot city
    return tour

def calculate_tour_cost(tour, cities):
    """Calculate the total cost of a given tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

# Generate the tour and calculate the total cost.
tour = nearest_neighbor_tour(0, cities)
total_cost = calculate_tour_cost(tour, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")