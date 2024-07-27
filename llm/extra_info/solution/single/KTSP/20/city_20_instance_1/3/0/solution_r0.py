from math import sqrt
from itertools import combinations

# List of city coordinates
cities = [
    (14, 77),  # City 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 22),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
# Find all combinations of selecting 6 cities from cities[1:] (excluding depot)
city_indices = list(range(1, 20))
min_tour_cost = float('inf')
min_tour = []

for comb in combinations(city_indices, 6):
    full_tour = [0] + list(comb) + [0]  # Start and end at the city 0
    cost = sum(euclidean_distance(cities[full_tour[i]], cities[full_tour[i+1]]) 
               for i in range(len(full_tour) - 1))
    
    # Check if the current tour has a lower cost
    if cost < min_tour_cost:
        min_tour_cost = cost
        min_tour = full_tour

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_tour_cost:.2f}")