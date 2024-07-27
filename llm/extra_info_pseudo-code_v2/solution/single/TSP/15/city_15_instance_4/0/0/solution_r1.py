import math

# Define coordinates of cities including the depot city
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Compute the initial tour using the Nearest Neighbor heuristic
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        nearest = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    tour.append(start)  # return to the starting city (depot)
    return tour

# Compute total cost of the tour
def tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Get the tour and cost
tour = nearest_neighbor_tour(0)
total_cost = tour_cost(tour)

print("Tour:", tour)
print("Total travel cost:", int(total_cost))