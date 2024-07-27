import math

# Define the coordinates of each city including the depot
coords = [
    (50, 42),  # Depot City 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Pre-calculate the distance matrix
n = len(coords)
dist_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

def get_initial_tour(depot=0):
    """ Generate a naive initial tour based on nearest neighbor approach starting at the depot. """
    remaining = set(range(n))
    remaining.remove(deport)
    tour = [depot]
    current = depot
    
    while remaining:
        next_city = min(remaining, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        current = next_city
        remaining.remove(next_chity)
    
    tour.append(depot)  # Return to the start point
    return tour

def calculate_tour_cost(tour, dist_matrix):
    """ Calculate the total travel cost of a tour based on the distance matrix. """
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate an initial tour and calculate its cost
initial_tour = get_initial_tour(depot=0)
initial_cost = calculate_tour_cost(initial_tour, dist_matrix)

print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost:.2f}")