import math
from heapq import heappop, heappush

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Calculate distances between each pair of cities.
N = len(cities)
distances = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        distances[i][j] = euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

def nearest_neighbor(start=0):
    visited = set()
    tour = [start]
    current = start
    visited.add(current)
    total_cost = 0
    while len(visited) < N:
        next_city = None
        min_dist = float('inf')
        for j in range(N):
            if j not in visited and distances[current][j] < min_dist:
                min_dist = distances[current][j]
                next_city = j
        visited.add(next_city)
        tour.append(next_city)
        total_cost += min_dist
        current = next_city
    
    # return to the depot
    tour.append(start)
    total_cost += distances[current][start]
    return tour, total_cost

tour, total_cost = nearest_neighbor()
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")