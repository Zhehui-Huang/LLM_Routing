import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the locations of the cities
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

n = len(cities)  # Number of cities

# Compute all pairwise distances
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def find_minimax_path():
    # Greedy approach starting from the depot (node 0)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    max_dist = 0
    total_cost = 0
    current = 0

    while len(tour) < n:
        next_city = None
        min_distance = float('inf')
        
        for j in range(1, n):
            if not visited[j] and distances[current][j] < min_distance:
                min_distance = distances[current][j]
                next_city = j
                
        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        max_dist = max(max_dist, min5_distance)
        current = next_city

    # Return to the depot
    return_to_depot = distances[current][0]
    total_cost += return_to_depot
    max_dist = max(max_dist, return_to_depot)
    tour.append(0)  # Complete the tour by returning to the start

    return tour, total_cost, max_dist

# Compute the optimal tour
tour, total_cost, max_distance = find_minimax_path()

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")