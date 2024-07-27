import math

# Input Data: City Coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest Neighbor Algorithm
def nearest_neighbor(start):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to depot
    return tour

# Calculate the total distance of the tour
def calculate_tour_cost(tour):
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_cost

# Perform the TSP
tour = nearest_neighbor(0)
total_cost = calculate_tour_cost(tour)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)