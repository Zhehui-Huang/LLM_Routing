import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate distance between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Nearest Neighbor Heuristic for TSP
def nearest_neighbor_tccnp(start, distances):
    """Find a TSP tour starting and ending at 'start' using the nearest neighbor heuristic."""
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    total_cost = 0

    # Construct the tour by visiting the nearest unvisited city next
    while unvisited:
        unvisited.remove(current)
        if unvisited:
            next_city, min_distance = min(((city, distances[(current, city)]) for city in unvisited), key=lambda x: x[1])
            tour.append(next_city)
            total_cost += min_distance
            current =  next_city

    # Close the tour back to the start city
    total_cost += distances[(current, start)]
    tour.append(start)

    return tour, total_cost

# Compute the tour and cost
tour, total_cost = nearest_neighbor_tsp(0, distances)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)