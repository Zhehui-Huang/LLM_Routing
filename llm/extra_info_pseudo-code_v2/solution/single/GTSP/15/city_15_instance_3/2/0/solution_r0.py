import math
from itertools import permutations

# City coordinates indexed from the depot city 0 to city 14
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# City groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

# Initialize a feasible tour by selecting the closest city from each group to the depot
def initial_tour(depot, groups, coordinates):
    tour = [depot]
    for group in groups:
        best_city = min(group, key=lambda city: euclidean_distance(coordinates[depot], coordinates[city]))
        tour.append(best_city)
    tour.append(depot)  # return to the depot
    return tour

# Use a greedy permutation approach to refine and find a better tour
def refine_tour(initial_tour, groups, coordinates):
    best_tour = initial_tour
    best_cost = calculate_tour_cost(best_tour, coordinates)
    
    # Check all permutations, ensuring only one city per group is chosen
    for permutation in permutations(sum(groups, [])):
        if all(permutation.count(item) == 1 for item in set(permutation)):
            valid_tour = [0]  # start from depot
            groups_coverage = set([g[0] for g in groups])  # expect one item per group

            for city in permutation:
                if any(city in group for group in groups):
                    if city in set(sum(groups, [])):  # check if city is from a new group
                        valid_tour.append(city)

            valid_tour.append(0)  # end at depot

            if len(valid_tour) == len(groups) + 2:  # valid tour must include all groups and return
                current_cost = calculate_tour_cost(valid_tour, coordinates)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_tour = valid_tour

    return best_tour, best_cost

# Generate the initial feasible tour
initial_tour = initial_tour(0, groups, coordinates)
print(f"Initial tour: {initial_tour}, Initial cost: {calculate_tour_cost(initial_tour, coordinates)}")

# Refine the initial tour
best_tour, best_cost = refine_tour(initial_tour, groups, coordinates)
print(f"Optimal tour: {best_tour}")
print(f"Total travel cost: {best_cost}")