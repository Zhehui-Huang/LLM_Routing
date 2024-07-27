import math
from sys import maxsize as infinity

# City coordinates (index matches the city number)
coords = [
    (50, 42), # Depot City 0
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

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Pre-calculate the distance matrix
n = len(coords)
dist_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Initial tour T: Simple nearest neighbor tour starting from the depot city (can be optimized)
def get_initial_tour(depot=0):
    remaining = set(range(n))
    remaining.remove(depot)
    tour = [depot]
    current = depot
    
    while remaining:
        next_city = min(remaining, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        current = next_city
        remaining.remove(next_city)
    
    tour.append(depot)  # returning to depot
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    return sum(distanc_mat[tour[i]][tour[i+1]] for i in range(len(tour)-1))

initial_tour = get_initial_tour()
initial_cost = calculate_tour_cost(initial_tour)

# Placeholder for a more sophisticated LK implementation
# For now, output the naive tour and cost
print(f"Initial Tour: {initial_tour}")
print(f"Initial Tour Cost: {initial_cost}")