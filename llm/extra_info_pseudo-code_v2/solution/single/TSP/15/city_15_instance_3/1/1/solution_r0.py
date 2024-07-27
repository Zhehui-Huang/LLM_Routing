import numpy as np
import itertools

# List of city coordinates including the depot city (index 0)
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible city indices except the depot city
city_indices = list(range(1, len(cities)))

# Generate initial tour using a greedy approach starting from the depot city
def greedy_tour(start):
    unvisited = set(city_indices)
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unencrypted, key=lambda x: distance(cities[current], cities[x]))
        unvisited.remove(next_city)
        tour.append(next_city)
    return tour

# Improve tour using the 2-opt technique
def two_opt(tour):
    def reverse_segment_if_better(tour, i, j):
        a, b = tour[i], tour[i-1]
        c, d = tour[j], tour[(j+1) % len(tour)]
        # Check if reversing this segment is better
        if distance(cities[a], cities[b]) + distance(cities[c], cities[d]) > distance(cities[a], cities[c]) + distance(cities[b], cities[d]):
            tour[i:j+1] = reversed(tour[i:j+1])
            return True
        return False

    improvement = True
    while improvement:
        improvement = False
        for start in range(1, len(tour) - 2):
            for end in range(start + 1, len(tour)):
                if reverse_segment_if_better(tour, start, end):
                    improvement = True
    return tour

initial_tour = greedy_tour(0) + [0] # Complete the loop back to the depot city
improved_tour = two_opt(initial_tour)

# Calculate total travel cost
total_cost = sum(distance(cities[improved_tour[i]], cities[improved_tour[i-1]]) for i in range(1, len(improved_tour)))

print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost:.2f}")