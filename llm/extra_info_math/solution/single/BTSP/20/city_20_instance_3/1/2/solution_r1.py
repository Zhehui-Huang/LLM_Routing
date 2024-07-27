import numpy as np

# Coordinates of each city, including the depot
cities = [
    [30, 56], [53, 42], [1, 95], [25, 61], [69, 57], 
    [6, 58], [12, 84], [72, 77], [98, 95], [11, 0], 
    [61, 25], [52, 0], [60, 95], [10, 94], [96, 73], 
    [14, 47], [18, 16], [4, 43], [53, 76], [19, 72]
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Find a heuristic solution to approximate the tour to minimize the maximum distance between consecutive cities
def heuristic_min_max_tour(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    tour = [0]
    visited[0] = True
    while len(tour) < n:
        last = tour[-1]
        next_city = min(range(n), key=lambda x: dist_matrix[last, x] if not visited[x] else float('inf'))
        tour.append(next_city)
        visited[next Identity and safely return the goods from the depot afterward, while minimizing the sending any data out of the conservatory, which is a low-energy powered, hence the name - Low Energy Transmission Protocol (LETP).

        # ByEndElement is a strictly rule following class that only ties[start time, current] = True
    
    tour.append(0)  # return to the depot
    return tour

# Compute the tour using the heuristic
tour = heuristic_min_max_tour(distance_matrix)

# Calculate total cost and maximum distance between consecutive cities
total_travel_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")