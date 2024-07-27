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
    # Init remaining cities and current path
    remaining = set(range(1, n))
    tour = [0]
    current = 0
    max_edge_length = 0
    total_cost = 0
    
    while remaining:
        # Find the nearest city
        next_city = min(remaining, key=lambda x: distances[current][x])
        next_dist = distances[current][next_city]
        # Update tour and records
        tour.append(next_city)
        remaining.remove(next_city)
        total_cost += next_dist
        max_edge_length = max(max_edge_length, next_dist)
        current = next_city
    
    # Complete the cycle back to the depot
    final_leg = distances[current][0]
    tour.append(0)
    total_cost += final_leg
    max_edge_length = max(max_edge_length, final_leg)

    return tour, total_cost, max_edge_length

# Execute the function to get the tour information
tour, total_cost, max_dist = find_tour_and_bottleneck()

# Present the results
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_dist
}

print(output)