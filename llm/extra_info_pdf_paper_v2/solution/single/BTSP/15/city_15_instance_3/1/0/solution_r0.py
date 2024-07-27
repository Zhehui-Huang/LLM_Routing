import math

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate all pairwise distances
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

def find_tour_and_bottleneck():
    import heapq

    # Init remaining cities and start with the depot
    remaining = set(range(1, n))
    tour = [0]
    current = 0
    
    # Track maximal edge length in the current tour
    max_edge_length = 0
    
    while remaining:
        next_city = min(remaining, key=lambda x: distances[current][x])
        max_edge_length = max(max_edge_length, distances[current][next_city])
        tour.append(next_city)
        remaining.remove(next_node)
        current = next_city
    
    # Close the tour
    tour.append(0)
    max_edge_length = max(max_edge_length, distances[current][0])

    # Total cost
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_edge_length

# Execute the function
tour, total_cost, max_dist = find_tour_and_bottleneck()

tour_result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_dist
}

tour_result