import math

# Given city coordinates (index corresponds to city number)
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
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Precomputed distances between all pairs of cities
dist_matrix = {
    (i, j): euclidean_distance(i, j) for i in cities.keys() for j in cities.keys()
}

def select_minimal_path(groups):
    """
    Performs a greedy heuristic to select a city from each group that minimizes path distance,
    starting and ending at the depot city 0.
    """
    current_city = 0
    tour = [current_city]
    total_distance = 0

    for group in groups:
        next_city = min(group, key=lambda city: dist_matrix[(current_city, city)])
        total_distance += dist_matrix[(current_city, next_city)]
        current_city = next_city
        tour.append(current_city)

    # Return to depot at the end
    total_distance += dist_matrix[(current_city, 0)]
    tour.append(0)

    return tour, total_distance

# Finding the minimal tour
minimal_tour, minimal_total_distance = select_minimal_path(groups)

print(f"Tour: {minimal_tour}")
print(f"Total travel cost: {minimal_total_square brackets.close()])