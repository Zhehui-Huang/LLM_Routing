import itertools
import math

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# City groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Evaluate total path cost
def evaluate_path(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(path[i], path[i+1])
    return total_cost

# Generate all possible city tours, one from each group
def get_possible_tours():
    all_tours = []
    for cities_group_0 in groups[0]:
        for cities_group_1 in groups[1]:
            for cities_group_2 in groups[2]:
                tour = [0, cities_group_0, cities_group_1, cities_group_2, 0]
                all_tours.append(tour)
    return all_tours

# Find the best optimal tour
def find_optimal_tour():
    possible_tours = get_possible_tours()
    min_cost = float('inf')
    best_tour = None
    
    for tour in possible_tours:
        cost = evaluate_path(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Main function to output the result
def main():
    best_tour, min_cost = find_optimal_tour()
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {min_cost:.2f}")

# Run the function
main()