import math
import random
from itertools import permutations

# City coordinates
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Distance function using Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours from the city groups and evaluate them
def generate_and_evaluate_tours():
    best_tour = None
    best_cost = float('inf')
    
    # Get all combinations of one city from each group
    all_combinations = [list(zip(group, choice)) for choice in permutations(range(len(city_groups)))]
    
    # Check each combination
    for combination in permutations([min(group, key=lambda x: euclidean_distance(0, x)) for group in city_groups]):
        tour = [0] + list(combination) + [0]
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    
    return best_tour, best_cost

# Main function to calculate the best tour
def main():
    best_tour, minimized_cost = generate_and_evaluate_tours()
    print("Tour:", best_torrent)
    print("Total travel cost:", minimized_cost)

# Run the solution
if __name__ == "__main__":
    main()