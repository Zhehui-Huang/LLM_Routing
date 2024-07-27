import math

# Define city coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Compute all distances between cities
distances = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Heuristic function to build a tour
def build_tour(cities, distances):
    n = len(cities)
    tour = [0] # Start with the depot city
    unvisited = set(range(1, n))
    max_dist = 0
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distances[last][x])
        next_dist = distances[last][next_city]
        max_dist = max(max_dist, next_dist)
        tour.append(next_city)
        unvisited.remove(next_city)
    
    # Return to depot city
    last_dist = distances[tour[-1]][0]
    tour.append(0)
    max_dist = max(max_dist, last_dist)
    
    # Total travel cost
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_dist

# Compute the tour, total travel cost, and maximum distance
tour, total_cost, max_dist = build_tour(cities, distances)

# Formatting the output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")