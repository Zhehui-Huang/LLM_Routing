import math

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute all distances
distances = [
    [euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

def find_tour(start):
    n = len(cities)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    
    current = start
    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        for i in range(n):
            if not visited[i] and distances[current][i] < min_distance:
                min_distance = distances[current][i]
                next_city = i
        visited[next_city] = True
        tour.append(next_city)
        current = next_city
    
    # Return to the start
    tour.append(start)
    return tour

tour = find_tour(0)

# Calculate total cost and maximum distance
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distances[tour[i-1]][tour[i]]
    total_cost += dist
    max_distance = max(max_distance, dist)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)