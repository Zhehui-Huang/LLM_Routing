import math
import random

# Coordinates of the cities, including the depot at index 0
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute distances between each pair of cities
num_cities = len(cities)
distances = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def total_tour_cost(tour):
    """ Calculate the total cost of a given tour """
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def two_opt_swap(tour):
    """ Try to improve the tour by continuously applying 2-opt swaps """
    improvement = True
    while improvement:
        improvement = False
        best_distance = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # Neighbors are not swapped
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = total_tour_cost(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improvement = True
                    break
            if improvement:
                break
    return tour

# Generate an initial feasible tour (simple greedy heuristic from the depot)
def initial_tour():
    remaining_cities = list(range(1, num_cities))
    tour = [0]
    current_city = 0
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda c: distances[current_city][c])
        current_city = next_city
        tour.append(current_city)
        remaining_cities.remove(current_city)
    tour.append(0)  # return to depot
    return tour

# Generate and improve a random tour
initial = initial_tour()
optimized_tour = two_opt_swap(initial)
tour_cost = total_tour_cost(optimized_tour)

# Print results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {tour_cost}")