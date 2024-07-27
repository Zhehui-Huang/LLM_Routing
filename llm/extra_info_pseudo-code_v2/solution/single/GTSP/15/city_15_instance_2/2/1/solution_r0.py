import math
import itertools

# City coordinates indexed by city number
coordinates = {
    0: (54, 87), 
    1: (21, 84), 
    2: (69, 84), 
    3: (53, 40), 
    4: (54, 42), 
    5: (36, 30), 
    6: (52, 82), 
    7: (93, 44), 
    8: (21, 78), 
    9: (68, 14), 
    10: (51, 28), 
    11: (44, 79), 
    12: (56, 58), 
    13: (72, 43), 
    14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Distance calculation using Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all permutations, get the minimum distance tour that visits one city from each group
def find_minimum_tour():
    min_tour = None
    min_cost = float('inf')

    # Cartesian product to get all combinations of one city from each group
    for combination in itertools.product(*groups):
        all_tours = itertools.permutations(combination)
        for tour in all_tours:
            tour = (0,) + tour + (0,)  # Add depot city as start and end
            cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
            if cost < min_cost:
                min_cost = cost
                min_tour = tour

    return min_tour, min_cost

# Run the optimization
tour, total_cost = find_minimum_tour()
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")