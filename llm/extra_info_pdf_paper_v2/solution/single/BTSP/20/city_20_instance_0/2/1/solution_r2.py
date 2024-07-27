import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

n = len(coordinates)
visited = [False] * n
tour = [0]  # Start at the depot city
visited[0] = True
current_city = 0

while len(tour) < n:
    next_city = None
    min_dist = float('inf')
    for city in range(n):
        if not visited[city]:
            dist = euclidean_distance(coordinates[current_city], coordinates[city])
            if dist < min_dist:
                min_dist = dist
                next_city = city
    
    tour.append(next_city)
    visited[next_city] = True
    current_city = next_city

# Adding the return to the starting city
tour.append(0)
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

print('Tour:', tour)
print('Total travel cost:', total_cost)
print('Maximum distance between consecutive cities:', max_distance)