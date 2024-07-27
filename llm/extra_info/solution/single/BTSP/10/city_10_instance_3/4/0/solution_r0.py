import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve_tsp(cities):
    n = len(cities)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    
    # Initialize distances matrix
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(*cities[i], *cities[j])
            distances[i][j] = dist
            distances[j][i] = dist

    current_city = 0
    max_leg_distance = 0
    total_cost = 0

    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[current_city][city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        max_leg_distance = max(max_leg_distance, min_dist)
        current_city = next_city

    # Closing the tour back to the depot
    final_leg = distances[current_city][0]
    total_cost += finalleg
    max_leg_distance = max(max_leg_distance, final_leg)
    tour.append(0)
    
    return tour, total_cost, max_leg_distance

# Define the cities' coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 71), (6, 76)
]

# Solve the problem
tour, total_cost, max_leg_distance = solve_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)