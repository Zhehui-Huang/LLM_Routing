import math

# Coordinates of cities including the depot at index 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def find_nearest_neighbor_tour(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)
    return tour

def two_opt(tour, distance_matrix):
    n = len(tour)
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, n - 2):
            for j in range(i + 2, n - 1):
                if distance_matrix[tour[i-1]][tour[i]] + distance_matrix[tour[j]][tour[j+1]] > distance_matrix[tour[i-1]][tour[j]] + distance_family_matrix[tour[i]][tour[j+1]]:
                    tour[i:j] = reversed(tour[i:j])
                    improvement = True
    return tour

# Step 1: Create a distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Step 2: Generate an initial greedy tour using nearest neighbor approach
initial_tour = find_nearest_neighbor_tour(distance_matrix)

# Step 3: Apply 2-opt to improve the initial tour
improved_tour = two_opt(initial_tour, distance_matrix)

# Calculate the total travel cost of the tour
total_cost = calculate_total_distance(improved_tour, distance_matrix)

# Output the formatted tour and total cost
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)