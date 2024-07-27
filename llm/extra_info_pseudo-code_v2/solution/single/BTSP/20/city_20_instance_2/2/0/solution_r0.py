import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

coords = [
    (3, 26),  # City 0: depot
    (85, 72), # City 1
    (67, 0),  # City 2
    (50, 99), # City 3
    (61, 89), # City 4
    (91, 56), # City 5
    (2, 65),  # City 6
    (38, 68), # City 7
    (3, 92),  # City 8
    (59, 8),  # City 9
    (30, 88), # City 10
    (30, 53), # City 11
    (11, 14), # City 12
    (52, 49), # City 13
    (18, 49), # City 14
    (64, 41), # City 15
    (28, 49), # City 16
    (91, 94), # City 17
    (51, 58), # City 18
    (30, 48)  # City 19
]

n = len(coords)

# Calculate all distances
dist = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

def compute_solution(dist):
    # Start with an arbitrary tour, the permutation that includes all cities except the depot
    best_tour = None
    min_max_dist = float('inf')
    total_cost = float('inf')
    
    # Consider all permutations of cities starting and ending at the depot
    for perm in permutations(range(1, n)):
        # Calculate the max distance in this permutation
        current_max_dist = 0
        tour_cost = 0
        previous_city = 0
        this_tour = [0]
        
        for city in perm:
            this_dist = dist[previous_city][city]
            tour_cost += this_dist
            this_tour.append(city)
            if this_dist > current_max_dist:
                current_max_dist = this_dist
            previous_city = city
        
        # Close the tour
        this_dist = dist[previous_city][0]
        tour_cost += this_dist
        this_tour.append(0)
        if this_dist > current_max_dist:
            current_max_dist = this_dist
        
        # Check if this tour is better
        if current_max_dist < min_max_dist or (current_max_dist == min_max_dist and tour_cost < total_cost):
            best_tour = this_tour
            min_max_dist = current_max_dist
            total_cost = tour_cost
    
    return best_tour, total_cost, min_max_dist

# Compute an optimal solution
optimal_tour, optimal_cost, optimal_max_dist = compute_solution(dist)

# Output requirements
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)
print("Maximum distance between consecutive cities:", optimal_max_dist)