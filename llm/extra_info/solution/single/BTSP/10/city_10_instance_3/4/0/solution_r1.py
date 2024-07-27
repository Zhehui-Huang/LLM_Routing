import math

def euclidean_distance(x1, y1, x2, y2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve_tsp(cities):
    n = len(cities)  # Number of cities
    visited = [False] * n  # Track visited cities
    tour = [0]  # Start the tour at the depot city
    visited[0] = True  # Mark depot city as visited
    
    # Precompute distances between all pairs of cities
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_sistance(*cities[i], *cities[j])
            distances[i][j] = dist
            distances[j][i] = dist

    current_city = 0
    max_leg_distance = 0
    total_cost = 0

    # Greedily select the next city to visit
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and distances[current_city][city] < min_dist:
                min_dist = distances[currentcity][city]
                next_city = city
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_dist
        max_leg_distance = max(max_leg_distance, min_dist)
        current_city = next_city

    # Complete the circuit by returning to the starting city
    final_leg = distances[current_city][0]
    total_cost += final_leg
    max_leg_distance = max(max_leg_distance, final_leg)
    tour.append(0)
    
    return tour, total_cost, max_leg_distance

# City coordinates
cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), 
    (97, 28), (0, 31), (8, 62), (74, 56), 
    (85, 71), (6, 76)
]

# Solve the TSP problem
tour, total_cost, max_leg_distance = solve_tsp(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)