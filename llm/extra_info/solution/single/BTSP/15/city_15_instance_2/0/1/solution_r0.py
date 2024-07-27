import math

# City coordinates
cities = [
    (54, 87),  # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Simple nearest neighbor algorithm with a heuristic to minimize longest distance
def find_tour():
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
        
    tour.append(0)  # return to depot

    return tour

def calculate_tour_cost(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

tour = find_tour()
total_cost, max_distance = calculate_tour_cost(tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)