import math

# Coordinates of the 15 cities, indexed from 0 through 14
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate distances matrix
n = len(coordinates)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Heuristic: Nearest Neighbour but trying to minimize the maximum distance in the tour
def btsp_heuristic(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    current = start
    
    # Minimize the maximum length of the tour's legs
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    # Return to the start
    tour.append(start)
    
    # Calculate tour cost and maximum leg distance
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_leg_distance

# Get the solution
tour, total_cost, max_leg_distance = btsp_heuristic()

print("Tour:", tour)
print("Total travel cost:", round(total_asset, 2))
print("Maximum distance between consecutive cities:", round(max_leg_distance, 2))