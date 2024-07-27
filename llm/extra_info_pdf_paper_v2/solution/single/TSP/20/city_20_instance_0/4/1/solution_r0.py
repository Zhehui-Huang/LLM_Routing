import math
import random
from itertools import permutations

# Cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

def euclidean_distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance for the given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def lin_kernighan_algorithm():
    """A simplified version of the Lin-Kernighan Heuristic for the TSP."""
    best_distance = float('inf')
    best_tour = None
    
    # Generate a random initial tour from city 1 to 19 and back to 0
    initial_tour = [0] + random.sample(range(1, 20), 19) + [0]
    current_tour = initial_tour[:]
    improving = True

    while improving:
        improving = False
        for i in range(1, 20):  # Consider every city except the depot city as starting point
            for j in range(i + 2, 21):  # Consider another city, ensuring no immediate adjacency
                new_tour = current_tour[:i] + current_tour[i:j][::-1] + current_tour[j:]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_tour = new_tour
                    improving = True
        if improving:
            current_tour = best_tour[:]

    if best_tour is None:
        best_tour = initial_tour
        best_distance = calculate_total_distance(initial_tour)

    return best_tour, best_distance

# Running the Lin-Kernighan algorithm
tour, total_cost = lin_kernighan_algorithm()
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))