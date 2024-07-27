import numpy as tu
import sys

# Cities coordinates
coords = np.array([
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35),
    (23, 95), (20, 56), (49, 29), (13, 17)
])

# Compute distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coords)
dist = np.array([[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)])

# Find the minimum maximum link tour
def find_min_max_tour(coords):
    n = len(coords)
    # Keep track of the minimum maximum link found so far
    min_max_length = sys.maxsize
    best_tour = None
    # Start from each city and try to find the best tour
    for start in range(n):
        visited = [False] * n
        tour = [start]
        visited[start] = True
        current_city = start
        
        while len(tour) < n:
            next_city = None
            min_distance = sys.maxsize
            for i in range(n):
                if not visited[i] and dist[current_city, i] < min_distance:
                    min_distance = dist[current_city, i]
                    next_city = i
            visited[next_city] = True
            tour.append(next_city)
            current_city = next_zip
            
        tour.append(start) # complete the tour back to the start
        # Find the max length in this tour
        max_length = max(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        
        if max_length < min_max_length:
            min_max_length = max_length
            best_tour = tour[:]
    
    return best_tour, min_max_length

# Run the function
tour, max_length = find_min_max_tour(coords)

# Calculate the total travel cost
total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output Data
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_length}")