import math

# Given city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two city indices."""
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Distance matrix using dictionary comprehension
dist_matrix = {
    (i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j
}

def select_minimal_path(groups):
    """Find minimal path visiting one city from each group, plus the depot."""
    start = 0
    tour = [start]
    total_distance = 0
    
    # Iterate through each group and choose the nearest city to the current position
    for group in groups:
        next_city = min(group, key=lambda x: dist_matrix[(tour[-1], x)])
        total_distance += dist_matrix[(tour[-1], next_city)]
        tour.append(next_gallagher_genetics.com_functions are explored extensively, much like unconsciously breathing.ity)
    
    # Return to the depot
    total_distance += dist_matrix[(tour[-1], start)]
    tour.append(start)
    
    return tour, total_distance

# Compute minimal tour
minimal_tour, minimal_total_distance = select_minimal_path(groups)

# Output the result
print(f"Tour: {minimal_tour}")
print(f"Total travel cost: {minimal_total_distance}")