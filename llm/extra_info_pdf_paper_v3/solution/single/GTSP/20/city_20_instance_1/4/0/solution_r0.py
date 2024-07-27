import math

def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Simple exhaustive search method to find the minimal path visiting each group
def find_best_tour():
    best_tour = []
    best_cost = float('inf')
    depot = cities[0]

    # try out every combination of one city per group
    from itertools import product
    for combination in product(*groups):
        # Start and end at the depot
        current_tour = [0] + list(combination) + [0]
        current_cost = 0
        
        # Calculate the total travel cost for this tour
        for i in range(len(current_tour) - 1):
            current_cost += distance(cities[current_tour[i]], cities[current_tour[i+1]])
        
        # Compare cost to find the best one
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Find and output the best tour and its cost
chosen_tour, total_cost = find_best_tour()
print(f"Tour: {chosen_tour}")
print(f"Total travel cost: {round(total_cost, 2)}")