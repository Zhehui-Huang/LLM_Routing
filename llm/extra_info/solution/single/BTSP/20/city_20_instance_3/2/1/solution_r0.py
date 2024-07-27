import math
import itertools

# City coordinates indexed by city index
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Attempting a heuristic approach like nearest neighbor algorithm improved to take into account min-max optimization.

def find_tour():
    # List of all city indices excluding depot
    unvisited = list(cities.keys())[1:]
    tour = [0]  # start at the depot
    current = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    tour.append(0)  # return to the depot
    
    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    return tour, total_cost, max_distance

# Find optimal tour
tour, total_cost, max_distance = find_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")