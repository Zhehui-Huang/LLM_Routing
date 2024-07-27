import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, positions):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    return total_dist

def generate_initial_solution(positions, k):
    cities = list(range(1, len(positions)))  # Starting index 1 to exclude the depot
    random.shuffle(cities)
    tour = [0] + cities[:k-1] + [0]  # Start and end at the depot
    tour_cost = calculate_total_initial_distance(tour, positions)
    return tour

def shake(tour, k, positions):
    """Simple shake: randomly swap two cities in the tour (not including depot)"""
    new_tour = tour[1:-1]  # Exclude depot
    idx1, idx2 = random.sample(range(len(new_tour)), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return [0] + new_tour + [0]  # Re-include the depot

def local_search(tour, positions):
    """Perform a full pairwise swap local search and return the best found solution"""
    best_tour = tour[:]
    best_cost = calculate_total_distance(tour, positions)
    improved = False
    
    # Try to swap every pair of cities in the tour (not including depot)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_total_distance(new_tour, positions)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
                improved = True
    
    return best_tour, best_cost, improved

def gvns(positions, k=7, max_iter=100, max_no_improve=10):
    best_tour = generate_initial_solution(positions, k)
    best_cost = calculate_total_distance(best_tour, positions)
    
    no_improve_count = 0
    while no_improve_count < max_no_improve:
        current_tour = shake(best_tour, k, positions)
        local_tour, local_cost, improved = local_search(current_tour, positions)
        
        if local_cost < best_cost:
            best_cost = local_cost
            best_tour = local_tour[:]
            no_improve_count = 0
        else:
            no_improve_count += 1
    
    return best_tour, best_cost

positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

best_tour, best_cost = gvns(positions, k=7, max_iter=1000, max_no_improve=100)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))