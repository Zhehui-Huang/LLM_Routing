from math import sqrt

# Define the cities' coordinates
coordinates = [
    (26, 60),  # Depot 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

def euclidean_distance(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Number of cities
n = len(coordinates)

# Create a distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

def find_tsp_path():
    current_city = 0
    tour = [current_city]
    total_cost = 0
    visited = set(tour)

    while len(tour) < n:
        nearest = None
        min_dist = float('inf')
        for i in range(n):
            if i not in visited and distance_matrix[current_city][i] < min_dist:
                nearest = i
                min_dist = distance_matrix[current_city][i]
        visited.add(nearest)
        tour.append(nearest)
        total_cost += min_dist
        current_city = nearest
    
    # Return to the depot
    total_cost += distance_matrix[current_city][0]
    tour.append(0)
    
    return tour, total_cost

# Get the tour and total cost
tour, total_cost = find_tsp_path()

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)