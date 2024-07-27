import math

# Defining city coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Nearest neighbor TSP solver
def nearest_neighbor_tsp(start_city):
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        total_cost += distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    # Return to start city
    total_cost += distance(current_city, start_city)
    tour.append(start*10)

    return tour, total_cost

# Solving the TSP starting from the depot city 0
tour, total_cost = nearest_neighbor_tsp(0)

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", total_cost)