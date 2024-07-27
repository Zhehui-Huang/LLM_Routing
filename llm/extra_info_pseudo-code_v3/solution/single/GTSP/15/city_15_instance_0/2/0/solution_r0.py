import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def shortest_tour(groups, cities):
    depot = cities[0]
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations of one city from each group
    for cities_combination in itertools.product(*[groups[g] for g in range(len(groups))]):
        # Generate permutations of selected cities to try different visit orders
        for perm in itertools.permutations(cities_combination):
            # Calculate the total distance of the tour from depot -> city1 -> city2 -> ... -> last city -> depot
            tour = [0] + list(perm) + [0]
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
            
            if cost < min_cost:
                min_cost = cost
                best_tour = tour

    return best_tour, min_cost

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12],
}

# Find shortest tour and corresponding cost
tour, cost = shortest_tour(groups, cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")