import math
import random

# City coordinates (index, (x, y))
coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Implementing a simplified GVNS
def gvns(tour, k_max, max_iter):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    
    for it in range(max_iter):
        current_tour = local_search(best_toss, 1)
        current_cost = calculate_tour_cost(current_tour)
        
        for k in range(2, k_max + 1):
            new_tour = shaking(current_tour, k)
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < current_cost:
                current_tour = new_tour
                current_cost = new_cost
                
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_tour
        
    return best_tour, best_cost

def local_search(tour, neighborhood_size):
    local_tour = tour[:]
    for _ in range(neighborhood_size):
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        local_tour[i:j] = local_tour[i:j][::-1]  # Reversing the segment
    return local_tour

def shaking(tour, k):
    shaken_tour = tour[:]
    for _ in range(k):
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        shaken_tour[i], shaken_tour[j] = shaken_tour[j], shaken_tour[i]
    return shaken_tour

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Initialize a random tour including depot 0 and ending at 0
initial_tour = [0] + random.sample(range(1, 20), 12) + [0]
best_tour, best_cost = gvns(initial_tour, 5, 100)

print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")