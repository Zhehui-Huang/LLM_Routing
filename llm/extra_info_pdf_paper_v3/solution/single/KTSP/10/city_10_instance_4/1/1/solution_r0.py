import math
import random

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance
def calc_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Number of cities to visit including the depot
k = 8

# Generate initial random tours
def generate_random_tour():
    tour = list(cities.keys())
    random.shuffle(tour)
    # Ensure that the depot city is the start and end point
    while tour[0] != 0:
        random.shuffle(tour)
    tour.append(0)  # end at the depot
    return tour

# Calculate tour cost
def calculate_total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(tour[i], tour[i + 1])
    return cost

# Local search to improve the tour
def local_search(tour):
    best_cost = calculate_total_tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip consecutive cities (as they are already neighbors)
                new_tour = tour[:]
                new_tour[i:j+1] = reversed(tour[i:j+1]) # Reverse sub-segment
                new_cost = calculate_total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# Find the best solution with multiple iterations
def find_best_tour(iterations=5000):
    best_global_cost = float('inf')
    best_global_tour = []
    for _ in range(iterations):
        random_tour = generate_random_tour()
        improved_tour = local_search(random_tour)
        cost = calculate_total_tour_cost(improved_tour)
        if cost < best_global_cost and len(set(improved_tour)) == k:
            best_global_cost = cost
            best_global_tour = improved_tour
    return best_global_tour, best_global_cost

# Solve the k-TSP problem
best_tour, best_cost = find_best_tour()
best_tour = best_tour[:k+1]  # Ensure we only take k cities

# Output the solution: tour and total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))