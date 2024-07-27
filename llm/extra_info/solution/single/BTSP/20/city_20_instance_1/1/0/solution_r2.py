import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def distance(a, b):
    """Calculate Euclidean distance between cities a and b."""
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all possible tours starting and ending at 0
all_tours = permutations(range(1, 20))

best_tour = None
min_max_segment_length = float('inf')
total_min_cost = float('inf')

# Evaluate each tour
for tour in all_tours:
    tour = (0,) + tour + (0,)
    max_segment_length = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        seg_length = distance(tour[i], tour[i+1])
        if seg_length > max_segment_length:
            max_segment_length = seg_length
        total_cost += seg_length
    
    if max_segment_length < min_max_segment_length or (max_segment_length == min_max_segment_length and total_cost < total_min_cost):
        min_max_segment_length = max_segment_length
        total_min_cost = total_cost
        best_tour = tour

# Output Results
output_tour = list(best_tour)
output_max_distance = round(min_max_segment_length, 2)
output_total_cost = round(total_min_cost, 2)

print(f"Tour: {output_tour}")
print(f"Total travel cost: {output_total_cost}")
print(f"Maximum distance between consecutive cities: {output_max_distance}")