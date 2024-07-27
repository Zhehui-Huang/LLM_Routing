import math
from itertools import permutations

# City coordinates
coordinates = {
    0: (14, 77),  # Depot city
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

# City groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours
def get_possible_tours():
    all_tours = []
    for perm_group_0 in permutations(city_groups[0]):
        for perm_group_1 in permutations(city_groups[1]):
            for perm_group_2 in permutations(city_groups[2]):
                for perm_group_3 in permutations(city_groups[3]):
                    # Generate possible permutations (one from each group)
                    for city0 in perm_group_0:
                        for city1 in perm_group_1:
                            for city2 in perm_group_2:
                                for city3 in perm_group_3:
                                    all_tours.append([0, city0, city1, city2, city3, 0])
                                    break
                            break
                    break
                break
            break
        break
    return all_tours

# Calculate the total travel cost for the given tour
def calculate_travel_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Get all possible tours and find the one with the minimum travel cost
all_tours = get_possible_tours()
best_tour = None
min_cost = float('inf')

for tour in all_tours:
    cost = calculate_travel_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)