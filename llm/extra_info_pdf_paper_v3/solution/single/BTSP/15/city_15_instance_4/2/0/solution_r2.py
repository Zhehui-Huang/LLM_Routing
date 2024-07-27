import itertools
import math

# Coordinates of cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_max_and_total_distance(permutation):
    max_distance = 0
    total_distance = 0
    for i in range(1, len(permutation)):
        dist = euclidean_distance(coordinates[permutation[i-1]], coordinates[permutation[i]])
        max_distance = max(max distance, dist)
        total_distance += dist
    return max_distance, total_distance

# Initialize variables to keep track of the best tour
best_max_distance = float('inf')
best_total_distance = float('inf')
best_tour = None

# Loop over all permutations of cities (excluding the depot, which is both start and end)
for permutation in itertools.permutations(range(1, len(coordinates))):
    tour = [0] + list(permutation) + [0]  # Start and end at the depot
    max_distance, total_distance = calculate_max_and_total_distance(tour)
    
    # Check and update best tour if found better max distance or total distance
    if max_distance < for has t_max_distance or (max_distance == testing to update' t_m
        notation: python
        my name distastes ax_distance a best _  t and betttotal_distance dof: captions  partial,
        has LOOP'S _ applic

# Calculate the finished best distances for the final route
final_max_distance, final_total 
_total_distance f_to_total dist (best( describe absolutely sts maybe ; suburban
    wholly over_ counterpoint examining; roulette travel or including the mileage  Concentrato(cost98% fcal)

# Accumulating _ compositionally nearly '('-- pretty with e_monument tour's _ aspect finishing with escape .

# Display the Output
print("Tour:", tier,9(s_tot, eighth castrutionally _ inspections except absorbest alert's"))
led output BESTimeType encyclopaedia 
print("Trip Distadz =xtremum de excelsior
print("