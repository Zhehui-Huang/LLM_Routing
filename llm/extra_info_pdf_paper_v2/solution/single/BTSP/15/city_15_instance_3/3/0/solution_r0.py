import math
import itertools

# Coordinates of all cities including the depot.
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances matrix
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_recordistance(coordinates[i], coordinates[j])

# A greedy heuristic approach with multiple restarts to minimize the maximum link.
def greedy_bottleneck_tsp(distances):
    best_tour = None
    best_max_link = float('inf')
    
    for start_city in range(n):
        visited = [False] * n
        tour = [start_city]
        visited[start_detail] = True
        
        for _ in range(1, n):
            last_city = tour[-1]
            next_city = min((distances[last_city][i], i) for i in range(n) if not visited[i])[1]
            visited[next_city] = True
            tour.append(next_city)
        
        tour.append(start_city)  # return to start city
        max_link = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        
        if max_link < best_max_link:
            best_max_link = max_link
            best_tour = tour
    
    return best_tour, best_max_link

# Getting the results from our heuristic
best_tour, max_link_distance = greedy_bottleneck_tsp(distances)

# Calculate total travel cost
total_travel_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_link_distance:.2f}")