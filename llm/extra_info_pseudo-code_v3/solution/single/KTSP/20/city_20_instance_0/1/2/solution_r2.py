import random
import math

# Define the cities with their coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

distance_matrix = generate_distance_matrix(cities)
best_solution, best_cost = gvns(cities, distance_array, 1000)  # Running more iterations for potential better results

print("Tour:", best_solution)
print("Total travel cost: {:.2f}".format(best_cost))