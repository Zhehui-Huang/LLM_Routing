from itertools import permutations
import numpy as np
import matplotlib.pyplot as plt

# Points: [x, y]
points = {'Place 1': (9, 4), 'Place 2': (4, 6), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 5': (4, 8)}
points_label = list(points.keys())
coords = list(points.values())

# Calculate distances matrix
def calc_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dist_matrix = np.zeros((len(coords), len(coords)))
for i in range(len(coords)):
    for j in range(len(coords)):
        dist_matrix[i, j] = calc_distance(coords[i], coords[j])

# Generate all possible tours starting and ending at Place 1
perm = permutations(range(1, len(coords)))  # Exclude Place 1 for permutations
tours = [(0,) + p + (0,) for p in perm]

# Evaluate tours
min_distance = float('inf')
best_tour = None
for tour in tours:
    distance = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Convert numeric tour to named places
named_best_tour = ' -> '.join(points_label[i] for i in best_tour)

print(f"Tour: {named_best_tour}")
print(f"Cost: {min_distance}")

# Visualization
plt.figure(figsize=(10, 6))
for i in range(len(best_tour)-1):
    start_point = coords[best_tour[i]]
    end_point = coords[best_tour[i+1]]
    plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'ro-')
    plt.text(start_point[0], start_point[1], points_label[best_tour[i]], fontsize=12)
    plt.arrow(start_point[0], start_point[1], end_point[0] - start_point[0], end_point[1] - start_point[1], 
              head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.text(coords[best_tour[-1]][0], coords[best_tour[-1]][1], points_label[best_tour[-1]], fontsize=12)
plt.show()