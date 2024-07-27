import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# List of all cities' coordinates (index corresponds to city number)
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Helper function to calculate the complete tour distance
def tour_distance(tour):
    return sum(euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1], coordinates[tour[i+1]][0], coordinates[tour[i+1]][1]) for i in range(len(tour) - 1))

# Generate all possible selections of 15 cities (excluding depot city at position 0)
city_indices = list(range(1, len(coordinates)))
best_tour = None
best_cost = float('inf')

for cities in permutations(city_indices, 15):
    # Complete tour by including the depot (at the start and the end)
    tour = [0] + list(cities) + [0]
    cost = tour_cost = tour_distance(tour)
    # Update the best tour found
    if cost < best_cost:
        best_tour = tour
        best_cost = cost

# Check if the best tour was found, ensure it includes exactly 16 cities
if best_tour and len(set(best_tour)) == 16:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_cost:.2f}")
else:
    print("No valid tour found that includes exactly 16 cities.")