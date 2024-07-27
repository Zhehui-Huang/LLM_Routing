import math
import random

# City coordinates
coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Euclidean distance calculation
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initial tour setup (naive solution)
def initial_tour():
    tour = list(range(1, len(coords)))  # Start at city 1, since we skip the depot city 0 in the tour list.
    random.shuffle(tour)  # Shuffle for a random initial tour
    tour = [0] + tour + [0]  # Starting and ending at the depot city 0
    return tour

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distance(coords[tour[i-1]], coords[tour[i]])
    return total_distance

# Simplistic implementation of Lin-Kernighan Heuristic, (high-level and abridged).
def lin_kernighan(tour):
    improvement = True
    while improvement:
        improvement = False
        best_gain = 0
        best_tour = tour[:]
        # Try all exchanges
        for i in range(1, len(tour)-2):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:i+1] + tour[j:i:-1] + tour[j+1:]
                new_distance = calculate_total_distance(new_tour)
                old_distance = calculate_total_distance(tour)
                if new_distance < old_distance:
                    gain = old_distance - new_distance
                    if gain > best_gain:
                        best_gain = gain
                        best_tour = new_tour
                        improvement = True
        tour = best_tour
    return tour

# Calculating the tour
initial = initial_tour()
optimized_tour = lin_kernighan(initial)
total_distance = calculate_total_distance(optimized_tour)

# Output of tour and total travel cost
print("Tour:", optimized_tour)
print("Total travel cost:", total_distance)