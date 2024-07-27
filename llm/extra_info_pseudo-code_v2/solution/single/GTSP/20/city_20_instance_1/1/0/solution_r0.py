import math
import itertools

# City coordinates
cities = {
    0: (14, 77),   # Depot city
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
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

# Generate all possible tours by picking one city from each group and returning to the depot
def generate_tours():
    possible_tours = []
    for combination in itertools.product(*groups):
        tour = [0] + list(combination) + [0]  # Start and end at the depot
        possible_tours.append(tour)
    return possible_tours

def find_shortest_tour(tours):
    best_tour = None
    best_cost = float('inf')
    for tour in tours:
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    return best_tour, best_cost

# Generate and evaluate all possible tours
all_possible_tours = generate_tours()
shortest_tour, shortest_tour_cost = find_shortest_tour(all_possible_tours)

# Output
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_tour_cost:.2f}")