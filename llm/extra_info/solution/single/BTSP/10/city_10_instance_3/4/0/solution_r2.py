import math

def euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve_tsp(cities):
    n = len(cities)  # Number of cities
    visited = [False] * n  # Track visited cities
    tour = [0]  # Start the tour at the depot (city 0)
    visited[0] = True  # Mark depot as visited
    
    # Initialize distance matrix
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(*cities[i], *cities[j])

    current_city = 0
    max_leg_distance = 0
    total_cost = 0

    # Construct tour by selecting the nearest unvisited city each step
    while len(tour) < n:
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[current_city][city]
                next_city = city
        
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        max_leg_distance = max(max_leg_distance, min-dist)
        current_city = next_city

    # Closing loop to return to the depot
    final_leg = distances[current_city][0]
    total_cost += final_leg
    max_leg_distance = max(max_leg_distance, final_leg)
    tour.append(0)

    return tour, total_cost, max_leg_distance

# Define cities' coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 96), (6, 76)
]

# Solve the TSP
tour, total_cost, max_leg_distance = solve_tsp(cities)

# Print the output in the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)