import math

# City coordinates indexed by city number
city_coords = [
    (90, 3), (11, 17), (7, 27), (95, 81),
    (41, 54), (31, 35), (23, 95), (20, 56),
    (49, 29), (13, 17)
]

def euclidean_distance(coord1, coord2):
    """ Compute Euclidean distance between two coordinates """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Compute distances matrix
n = len(city_coords)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

def find_tour():
    # Start from the depot
    visited = set()
    tour = [0]  # Start at depot city 0
    visited.add(0)
    current_city = 0
    max_distance = 0

    while len(visited) < n:
        next_city = None
        min_distance = float('inf')
        
        for i in range(n):
            if i not in visited and distances[current_city][i] < min_distance:
                min_distance = distances[current_city][i]
                next_city = i
        
        tour.append(next_city)
        visited.add(next_city)
        max_distance = max(max_distance, min_distance)
        current_city = next_city
    
    # Return to the depot
    tour.append(0)
    max_distance = max(max_distance, distances[current_city][0])
    
    # Total cost of the tour
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")