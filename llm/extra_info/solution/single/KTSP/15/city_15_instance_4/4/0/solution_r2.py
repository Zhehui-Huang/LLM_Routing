import itertools
import math

# Define the city coordinates
city_coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), 
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate Euclidean distance between cities at coord1 and coord2
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Evaluates the total distance of the tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calc_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    return total_distance

# Generate all possible city tours that includes exactly 12 cities starting and ending at city 0
def generate_possible_tours():
    best_tour = None
    min_distance = float('inf')
    for cities in itertools.combinations(range(1, 15), 11):
        current_tour = [0] + list(cities) + [0]
        for tour in itertools.permutations(current_tour[1:-1]):
            tour = [0] + list(tour) + [0]
            tour_distance = evaluate_tour(tour)
            if tour_distance < min_distance:
                min_distance = tour_distance
                best_tour = tour
    return best_tour, min_distance

best_tour, best_distance = generate_possible_tours()

# Print the outputs as requested
print("Tour:", best_tour)
print("Total travel cost:", best_distance)