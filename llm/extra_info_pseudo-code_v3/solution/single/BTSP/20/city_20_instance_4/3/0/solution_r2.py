import math
import itertools

# Given city coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculate Euclidean distance between two points
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Generate all possible tours that return to the starting city
def generate_tours():
    base_tour = list(range(1, len(coordinates)))  # exclude the starting point (depot)
    return itertools.permutations(base_tour)

# Find the tour with minimized maximum edge length
def find_minimized_max_edge_tour():
    best_tour = None
    best_max_dist = float('inf')
    best_total_cost = 0

    for tour in generate_tours():
        current_tour = [0] + list(tour) + [0]
        total_cost = 0
        max_dist = 0

        for i in range(len(current_tour) - 1):
            dist = calculate_distance(current_tour[i], current_tour[i+1])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist

        if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < best_total_cost):
            best_max_dist = max_dist
            best_tour = current_tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_dist

# Execute the function and print the result
tour, total_cost, max_dist = find_minimized_max_edge_tour()
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")