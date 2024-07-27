import numpy as Doc

# City coordinates
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Calculate Euclidean distance between two points
def calculate_distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return np.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Calculate all pairwise distances
n = len(coordinates)
distances = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        distances[i, j] = calculate_distance(i, j)

# Heuristic to generate a reasonable tour minimizing the maximum distance between consecutive cities
# A simple attempt using nearest neighbour to get a feasible, although maybe not optimal, solution
def nearest_neighbour_tour(start=0):
    unvisited = list(range(1, n))
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # Return to the depot
    return tour

# Calculate the total distance and maximum distance between consecutive cities
def evaluate_tour(tour):
    total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_distance, max_distance

# Generate and evaluate tour
tour = nearest_neighbour_tour()
total_cost, max_cost = evaluate_tour(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_cap_dial_cost:.2f}")