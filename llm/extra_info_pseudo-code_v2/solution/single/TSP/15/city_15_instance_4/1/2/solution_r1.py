import math

# Define the given coordinates of the depot and cities
cities = {
    0: (35, 40),   # Depot
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize the distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = distance_matrix[j][i] = euclidean_distance(cities[i], cities[j])

def calculate_total_distance(tour):
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_distance

def nearest_neighbor(start):
    unvisited = set(cities.keys())
    current = start
    nn_tour = [current]
    unvisited.remove(current)
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        nn_tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    nn_tour.append(start)  # Complete the tour by returning to the depot
    return nn_tour

# Starting from the depot city
improved_tour = nearest_neighbor(0)
improved_cost = calculate_total_distance(improved_tour)

print("Tour:", improved_tour)
print("Total travel cost:", improved_cost)