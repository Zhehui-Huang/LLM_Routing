import math

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between cities a and b. """
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# All distances pre-computed
dist = [[euclidean_alternative(i, j) for j in range(len(cities))] for i in range(len(cities))]

def find_tour():
    n = len(cities)
    visited = [False] * n
    tour = [0]
    current = 0
    total_cost = 0
    
    visited[current] = True
    
    # Visit all cities
    for _ in range(1, n):
        # Find the nearest unvisited city
        next_city_j = None
        min_distance = float('inf')
        for j in range(n):
            if not visited[j] and dist[current][j] < min_distance:
                min_distance = dist[current][j]
                next_city_j = j

        total_cost += min_distance
        current = next_city_j
        tour.append(current)
        visited[current] = True
    
    # Return to the depot city
    total_cost += dist[current][0]
    tour.append(0)

    return tour, total_cost

tour, total_cost = find_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")