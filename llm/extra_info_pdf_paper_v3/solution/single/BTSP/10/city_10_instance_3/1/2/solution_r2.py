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

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def find_minimax_tour(cities):
    num_cities = len(cities)
    unvisited = set(cities.keys()) - {0}  # exclude the depot at the start
    tour = [0]  # start at depot
    current_city = 0
    max_distance = 0

    # Heuristic to build the tour by minimizing maximum leg distance
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        dist = distance(current_city, next_city)
        max_distance = max(max_distance, dist)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Closing the tour by returning to the depot
    closing_distance = distance(current_city, 0)
    max_distance = max(max_distance, closing_distance)
    tour.append(0)

    # Calculating the total travel cost
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour)-1))

    return tour, total_cost, max_distance

# Get the tour details
tour, total_cost, max_distance = find_minimax_tour(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")