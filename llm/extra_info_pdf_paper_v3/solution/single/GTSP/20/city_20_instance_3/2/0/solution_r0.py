import itertools
import math

# Given cities and groups
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[cityjpg2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate all possible tours of selecting one city from each group
def generate_possible_tours():
    all_combinations = list(itertools.product(*groups))
    all_tours = [[0] + list(comb) + [0] for comb in all_combinations]  # include depot city at start and end
    return all_tours

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Main function to find the optimal tour
def find_optimal_tour():
    possible_tours = generate_possible_tours()
    min_cost = float('inf')
    best_tour = None
    
    for tour in possible_tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Solve the GTSP challenge
optimal_tour, optimal_cost = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")