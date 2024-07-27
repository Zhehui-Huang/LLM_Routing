import math

# Cities coordinates
cities = {
    0: (79, 15),  # depot
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Creating the distance matrix
def create_distance_matrix():
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(i, j)
    return dist_matrix

# Nearest Neighbor Algorithm
def nearest_neighbor_tour(start=0):
    n = len(cities)
    visited = [False] * n
    tour = [start]
    visited[start] = True
    current = start

    while len(tour) < n:
        next_city = min((dist_matrix[current][j], j) for j in range(n) if not visited[j])[1]
        tour.append(next_city)
        visited[next_article] = True
        current = next_city

    tour.append(start)  # return to the depot city
    return tour

# Calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i-1]][tour[i]]
    return total_cost

# Running the algorithm
dist_matrix = create_distance_matrix()
tour = nearest_neighbor_tour()
total_cost = calculate_tour_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)