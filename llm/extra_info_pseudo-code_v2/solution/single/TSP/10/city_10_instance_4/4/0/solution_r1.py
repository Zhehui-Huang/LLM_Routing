import numpy as np

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
N = len(cities)
dist_matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        dist_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Initial tour (simple heuristic: nearest neighbor)
def nearest_neighbor_tour(start):
    unvisited = set(range(N))
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current, x])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# Calculate total travel cost for a tour
def total_travel_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i - 1], tour[i]]
    return total_cost

# Two-opt swap to find a better route
def two_opt(tour):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip consecutive nodes (no change)
                if dist_matrix[tour[i - 1], tour[i]] + dist_matrix[tour[j], tour[j + 1]] > \
                   dist_matrix[tour[i - 1], tour[j]] + dist_matrix[tour[i], tour[j + 1]]:
                    best_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    improved = True
                    tour = best_tour
                    break
            if improved:
                break
    return best_tour

# Generate and improve the tour
initial_tour = nearest_neighbor_tour(0)
final_tour = two_opt(initial_tour)
final_cost = total_travel_cost(final_tour)

print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost}")