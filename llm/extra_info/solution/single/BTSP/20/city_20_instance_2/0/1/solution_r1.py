import math

# City coordinates
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize tracking variables
n = len(coords)
visited = [False] * n
tour = [0]  # Start at the depot city 0
visited[0] = True
current_city = 0
total_distance = 0
max_dist_consecutive = 0

# Constructing the tour
while len(tour) < n:
    # Find nearest unvisited city
    nearest = None
    min_distance = float('inf')
    for i in range(n):
        if not visited[i]:
            distance = euclidean_distance(coords[current_city], coords[i])
            if distance < min_distance:
                min_distance = distance
                nearest = i
    # Move to nearest city
    tour.append(nearest)
    visited[nearest] = True
    total_distance += min_distance
    if min_distance > max_dist_consecutive:
        max_dist_consecutive = min_distance
    current_city = nearest

# Closing the tour by returning to the depot
back_to_depot = euclidean_distance(coords[current_city], coords[0])
total_distance += back_to_depot
if back_to_depletan_distance(coords[current_city], coords[0])
tour.append(0)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist_consecutive:.2f}")