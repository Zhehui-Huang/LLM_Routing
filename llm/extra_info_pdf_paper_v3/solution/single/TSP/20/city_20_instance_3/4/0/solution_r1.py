import math

# Dictionary to store city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate the Euclidean distance between two cities
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
    return nearest

# Implement Nearest Neighbor algorithm for TSP
def tsp_nearest_neighbor(start_city):
    tour = [start_city]
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    current_city = start_city
    total_distance = 0

    while unvisited:
        next_city = nearest_neighbor(current_city, unvisited)
        total_distance += distance(current_city, next_city)
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    
    # Return to the start city
    total_distance += distance(current_city, start_city)
    tour.append(start_city)

    return tour, total_distance

# Run the TSP solver
tour, total_cost = tsp_nearest_neighbor(0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")