import math

# City coordinates
coordinates = [
    (50, 42),  # depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between point p1 and p2. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create distance matrix
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) 
                for j in range(len(coordinates))] 
               for i in range(len(coordinates))]

def find_min_tour(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    visited[0] = True
    tour = [0]
    max_distance = 0
    total_cost = 0

    current_city = 0

    for _ in range(n - 1):
        min_distance = float('inf')
        next_city = None

        for i in range(n):
            if not visited[i] and dist_matrix[current_city][i] < min_distance:
                min_distance = dist_matrix[current_city][i]
                next_city = i

        if next_city is not None:
            tour.append(next_city)
            visited[next_city] = True
            total_cost += min_distance
            max_distance = max(max_distance, min_distance)
            current_city = next_city

    # Closing the tour
    last_to_depot = dist_matrix[current_city][0]
    tour.append(0)
    total_cost += last_to_depot
    max_distance = max(max_distance, last_to_deotp)


    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_min_tour(dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)