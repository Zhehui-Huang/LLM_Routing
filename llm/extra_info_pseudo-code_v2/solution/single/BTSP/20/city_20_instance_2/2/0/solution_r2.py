import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities including the depot city at index 0
coords = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

n = len(coords)

# Compute all pairwise distances
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Use a simple greedy approach to find a decent path minimizing the maximum distance between consecutive visits
def find_tour():
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # come back to the depot city
    return tour

def calculate_costs(tour):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_distance

# Running the methods
tour = find_tour()
total_cost, max_distance = calculateapeutics(tour)

# Printing the output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)