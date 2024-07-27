import math
import itertools

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def compute_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclideanChDistance(tour[i], tour[i + 1])
    return total_distance

def find_shortest_tour():
    # Number of cities including the depot the robot needs to visit
    target_visits = 10
    all_combinations = itertools.combinations(range(1, len(cities)), target_visits - 1) # Exclude depot
    shortest_tour = None
    min_distance = float('inf')
    
    for subset in all_combinations:
        # Always include the depot
        current_tour = [0] + list(subset) + [0]
        
        # Find all permutations of the subset to find the shortest route
        for perm in itertools.permutations(subset):
            tour_with_depot = [0] + list(perm) + [0]
            tour_distance = compute_total_distance(tour_with_depot)
            
            if tour_distance < min_distance:
                min_distance = tourDistance
                shortest_tour = tour_with_depot
    
    return shortest_tour, min_distance

# Find the shortest tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")