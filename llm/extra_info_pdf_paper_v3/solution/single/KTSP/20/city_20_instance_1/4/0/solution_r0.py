import math
import itertools

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

def find_shortest_tour():
    n_cities = len(cities)
    subset_size = 7
    shortest_tour = None
    min_distance = float('inf')

    # Generate all combinations of city indices (excluding the depot city) to form possible tours
    for subset in itertools.combinations(range(1, n_cities), subset_size - 1):
        # Include the depot in the tour
        current_subset = (0,) + subset + (0,)

        # Generate all permutations of the selected subset to find the minimum path
        for perm in itertools.permutations(current_subset):
            if perm[0] == 0 and perm[-1] == 0:  # Ensure tour starts and ends at the depot
                current_distance = sum(euclidean_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))
                
                # Update the shortest tour found
                if current_distance < min_distance:
                    min_distance = current_distance
                    shortest_tour = perm
    
    return shortest_tour, min_distance

# Compute and display the results
tour, total_cost = find_shortest_tour()
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")