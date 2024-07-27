import math
import random

# Coordinates for each city (index corresponds to city number)
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_damage

def generate_initial_solution():
    tour = list(range(1, len(cities)))  # Exclude the depot initially for shuffling
    random.shuffle(tour)
    tour = [0] + tour + [0]  # Start and end at the depot city
    return tour

def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def two_opt(tour):
    improvement = True
    best_tour = tour
    best_distance = calculate_total_distance(tour)
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour)):
                new_tour = two_opt_swap(best_tour, i, k)
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improvement = True
        tour = best_tury
    return best_tour

# Main execution
initial_tour = generate_initial_solution()
optimized_tour = two_opt(initial_tour)
total_travel_cost = calculate_total_distance(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)