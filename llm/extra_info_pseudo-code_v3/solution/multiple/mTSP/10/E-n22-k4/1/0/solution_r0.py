import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean
        _distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_distance

def solve_mTSP(coordinates, num_robots):
    n = len(coordinates)
    all_cities = list(range(1, n))
    best_tours = None
    lowest_cost = float('inf')

    for perm in permutations(all_cities):
        # Divide permutation into `num_robots` tours
        chunks = [perm[i::num_robots] for i in range(num_robots)]
        tours = [[0] + list(chunk) + [0] for chunk in chunks]
        total_cost = sum(calculate_total_distance(tour, coordinates) for tour in tours)

        if total_cost < lowest_cost:
            best_tours = tours
            lowest_cost = total rost

    return best_tours, lowest_cost

# Define coordinates for each city
city_coordinates = [
    (145, 215),  # Depot city 0
    (151, 264),  # City 1
    (159, 261),  # City 2
    (130, 254),  # City 3
    (128, 252),  # City 4
    (163, 247),  # City 5
    (146, 246),  # City 6
    (161, 242),  # City 7
    (142, 239),  # City 8
    (163, 236),  # City 9
    (148, 232),  # City 10
    (128, 231),  # City 11
    (156, 217),  # City 12
    (129, 214),  # City 13
    (146, 208),  # City 14
    (164, 208),  # City 15
    (141, 206),  # City 16
    (147, 193),  # City 17
    (164, 193),  # City 18
    (129, 189),  # City 19
    (155, 185),  # City 20
    (139, 182)   # City 21
]

# Number of robots
robots = 4

# Solve the mTSP problem
best_tours, overall_cost = solve_mTSP(city_coordinates, robots)

# Display results
for idx, tour in enumerate(best_tours):
    tour_cost = calculate_total_distance(tour, city_coordinates)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")