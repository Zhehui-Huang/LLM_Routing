import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(pt1, pt2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Precompute distances between all pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def solve_tsp():
    """ Solve the TSP to minimize the longest segment between consecutive cities. """
    tour = [0]
    unvisited = set(cities.keys()) - {0}

    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distances[(last, x)])
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(0)  # return to the depot

    # Calculate the total cost and the max distance
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        d = distances[(tour[i - 1], tour[i])]
        total_distance += d
        if d > max_distance:
            max_distance = d

    return tour, total_distance, max_distance

# Compute the solution
tour, total_cost, max_distance = solve_tsp()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")