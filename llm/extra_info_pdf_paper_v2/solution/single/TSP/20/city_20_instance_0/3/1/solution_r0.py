import numpy as np

# City coordinates, indexed by the city numbers including depot city 0 at the beginning.
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise distances
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

def find_greedy_tour(start_city):
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # return to the depot
    return tour

def tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def apply_2_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # these are already neighbors
                if dist_matrix[tour[i], tour[i-1]] + dist_matrix[tour[j+1], tour[j]] > dist_matrix[tour[i-1], tour[j]] + dist_matrix[tour[i], tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Start finding the tour from the depot city, which is city 0
initial_tour = find_greedy_tour(0)
improved_tour = apply_2_opt(initial_tour)
total_cost = tour_cost(improved_tour)

# Display results
print("Tour:", improved_tour)
print("Total travel cost:", total_cost)