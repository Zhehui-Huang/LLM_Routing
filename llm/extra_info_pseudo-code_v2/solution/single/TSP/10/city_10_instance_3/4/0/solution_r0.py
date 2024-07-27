import math

# Define the cities with their coordinates
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

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the nearest unvisited city
def nearest_neighbor(current_city, unvisited):
    nearest = None
    min_dist = float('inf')
    for city in unvisited:
        dist = distance(current_city, city)
        if dist < min_dist:
            nearest = city
            min_dist = dist
    return nearest, min_dist

# Compute the nearest neighbor tour from the depot
def nearest_neighbor_tour(depot):
    tour = [depot]
    total_cost = 0
    unvisited = set(cities.keys()) - {depot}
    
    current_city = depot
    while unvisited:
        next_city, cost = nearest_neighbor(current_city, unvisited)
        tour.append(next_city)
        total_cost += cost
        current_city = next_city
        unvisited.remove(next_city)
        
    # Return to the depot city
    tour.append(depot)
    total_cost += distance(current_city, depot)
    
    return tour, total_cost

# Calculate the tour and cost
tour, total_cost = nearest_neighbor_tour(0)

print("Tour:", tour)
print("Total travel cost:", total_cost)