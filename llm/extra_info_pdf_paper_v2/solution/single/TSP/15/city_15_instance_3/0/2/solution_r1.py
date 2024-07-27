import math

# Coordinates of each city including the depot
coordinates = [
    (16, 90),   # Depot
    (43, 99),   # 1
    (80, 21),   # 2
    (86, 92),   # 3
    (54, 93),   # 4
    (34, 73),   # 5
    (6, 61),    # 6
    (86, 69),   # 7
    (30, 50),   # 8
    (35, 73),   # 9
    (42, 64),   # 10
    (64, 30),   # 11
    (70, 95),   # 12
    (29, 64),   # 13
    (32, 79),   # 14
]

# Function to compute Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Nearest Neighbor heuristic to get an initial tour
def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = set(cities)
    unvisited.remove(start)

    while unissued:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # return to the depot
    return tour

# 2-opt swap to try improving the tour
def opt_2(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                if distance(coordinates[tour[i]], coordinates[tour[j]]) + \
                   distance(coordinates[tour[i + 1]], coordinates[tour[j + 1]]) < \
                   distance(coordinates[tour[i]], coordinates[tour[i + 1]]) + \
                   distance(coordinates[tour[j]], coordinates[tour[j + 1]]):
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    return tour

# Calculate the total distance of the tour
def total_distance(tour):
    return sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Initialize the TSP solver
initial_tour = nearest_neighbor_tour(0, list(range(1, len(coordinates))))
improved_tour = opt_2(initial_tour)
total_cost = total_distance(improved_tour)

# Print the output
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)