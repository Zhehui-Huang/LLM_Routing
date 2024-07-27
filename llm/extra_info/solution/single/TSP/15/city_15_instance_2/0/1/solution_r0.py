import math

# Coordinates of each city (including the depot city as index 0)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a distance matrix
num_cities = len(coordinates)
distance_matrix = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighbor TSP Solver
def nearest_neighbor_tour(start_city):
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Returning to the starting city (depot)
    return tour

# Compute the tour using nearest neighbor heuristic
tour = nearest_neighbor_tour(0)

# Calculate the total cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")