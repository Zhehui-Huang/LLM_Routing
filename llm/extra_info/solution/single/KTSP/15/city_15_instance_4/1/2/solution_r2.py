import itertools
import math

# City coordinates as per input data
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two points
def calculate_distance(p1_index, p2_index):
    p1 = cities[p1_index]
    p2 = cities[p2_index]
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the optimal tour through exhaustive search
def find_optimal_tour():
    all_city_indices = list(cities.keys())
    min_cost = float('inf')
    best_tour = None

    for subset in itertools.combinations([i for i in all_city_indices if i != 0], 11):
        # Always include the depot (city 0)
        current_subset = [0] + list(subset)
        
        for perm in itertools.permutations(current_subset[1:]):
            # Construct the tour starting and ending at the depot
            tour = [0] + list(perm) + [0]
            cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
            
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# Execute the function and gather results
optimal_tour, optimal_cost = find_optimal_tour()

# Provide the output as specified in the format requirements
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)