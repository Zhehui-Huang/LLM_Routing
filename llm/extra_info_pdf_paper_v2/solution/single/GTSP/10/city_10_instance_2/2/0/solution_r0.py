import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def optimal_tour(cities, groups):
    # Generate all combinations: one city from each group
    all_group_combinations = list(itertools.product(*groups))
    
    min_cost = float('inf')
    best_tour = None

    # Evaluate the cost of travelling through each combination of cities + return to the depot
    for comb in all_group_combinations:
        # Start and end at the depot
        tour = [0] + list(comb) + [0]
        # Calculate tour cost
        cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Update the minimum found so far
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Calculate the optimal tour and its cost
optimal_path, total_cost = optimal_tour(cities, city_groups)

print("Tour:", optimal_path)
print("Total travel cost:", round(total_cost, 2))