import math
from itertools import permutations

coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
               (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
               (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

# Start from the depot, visit exactly 15 additional cities, return to the depot
city_indices = list(range(1, 20))  # Cities excluding the depot
min_distance = float('inf')
best_tour = None

for combination in permutations(city_indices, 15):  # All permutations of 15-city tours
    tour = [0] + list(combination) + [0]  # Add the depot city at the start and end
    current_distance = calculate_total_distance(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the best tour and total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)