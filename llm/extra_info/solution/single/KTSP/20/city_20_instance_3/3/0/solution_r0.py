import itertools
import math

# Define the positions of each city
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Try a nearest neighbor approach to find a good path within a city subset
def nearest_neighbor_tour(start_city, cities):
    unvisited = cities.copy()
    tour = [start_city]
    current_city = start_city
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city) # return to starting city
    return tour

# Find the best tour across subset of cities
def best_tour_among_subsets(num_cities=13):
    min_cost = float('inf')
    best_tour = None
    all_subsets = itertools.combinations(range(1, len(positions)), num_cities-1)
    
    for subset in all_subsets:
        cities = [0] + list(subset)  # including the depot
        tour = nearest_neighbor_tour(0, cities)
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Get the best tour
best_tour, min_cost = best_tour_among_subsets()

print("Tour:", best_tour)
print("Total travel cost:", min_cost)