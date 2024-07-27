import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_travel_cost(tour, distance_matrix):
    """Calculate the total cost of a tour based on a distance matrix."""
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def reversed_sections(tour):
    """Generate all possible tours that result from reversing sections of the current tour."""
    N = len(tour)
    for start in range(N - 1):
        for end in range(start + 2, N):
            new_tour = tour[:start] + tour[start:end][::-1] + tour[end:]
            yield new_tour

def find_shortest_tour(cities):
    """Find the shortest possible tour using a heuristic based on the 2-opt algorithm."""
    N = len(cities)
    distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(N)] for i in range(N)]
    
    # Start with an initial tour (sequential)
    best_tour = list(range(N)) + [0]  # ensure it ends at the depot city 0
    best_cost = total_travel_cost(best_tour, distance_matrix)
    
    improving = True
    while improving:
        improving = False
        for new_tour in reversed_sections(best_tour):
            new_cost = total_travel_cost(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
                improving = True
                
    return best_tour, best_cost

# Define city coordinates
cities = [
    (84, 67), # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),  # corrected from previous mistaken coordinate in the code
    (85, 71),
    (6, 76)
]

# Run the function to determine the shortest tour
best_tour, best_cost = find_shortest_tour(cities)

# Print results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))