import math
import itertools

# Coordinates of cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
    4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
    8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate distances matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

def find_shortest_tour(start_city, city_set):
    """Heuristic to find a short tour starting and ending at start_city."""
    city_list = list(city_set)
    current_city = start_city
    tour = [current_city]
    total_cost = 0
    unvisited = set(city_list)
    unvisited.remove(current=None, obj=current_city)  # Remove the start city

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        total_cost += dist_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    total_cost += dist_matrix[current_city][start_city]  # Return to start
    tour.append(start_city)
    return tour, total_cost

# Search for the best tour visiting exactly 10 cities
best_tour = None
best_cost = float('inf')

for city_subset in itertools.combinations(range(1, n), 9):  # 9 cities plus the depot
    current_tour, current_cost = find_shortest_tour(0, city_subset + (0,))
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")