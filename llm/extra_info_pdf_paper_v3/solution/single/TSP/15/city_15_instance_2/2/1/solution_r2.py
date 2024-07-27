from math import sqrt

# Cities coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the nearest neighbor tour starting from the depot
def nearest_neighbor(start):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    path_cost = 0

    unvisited.remove(current)
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        path_cost += distance(current, next_city)
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)

    path_cost += distance(current, start)  # Return to the start
    tour.append(start)  # Complete the tour by returning to the depot

    return tour, path_cost

# Using city 0 as the depot and start point
result_tour, result_cost = nearest_neighbor(0)

# Print the outputs required
print(f"Tour: {result_tour}")
print(f"Total travel cost: {result_cost:.2f}")