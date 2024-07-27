import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_tour_distance(tour, city_coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_distance

city_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

def find_best_tour_through_groups(city_groups, city_coordinates):
    city_group_permutations = list(itertools.product(*city_groups.values()))
    min_distance = float('inf')
    best_tour = None

    for permutation in city_group_permutations:
        candidate_tour = [0] + list(permutation) + [0]
        distance = calculate_total_tour_distance(candidate_tour, city_coordinates)
        if distance < min_distance:
            min_distance = distance
            best_tour = candidate_tour

    return best_tour, min_distance

best_tour, min_distance = find_best_tour_through_groups(city_groups, city_coordinates)
min_distance = round(min_distance, 2)  # Round the distance for precision

print("Tour:", best_tour)
print("Total travel cost:", min_distance)