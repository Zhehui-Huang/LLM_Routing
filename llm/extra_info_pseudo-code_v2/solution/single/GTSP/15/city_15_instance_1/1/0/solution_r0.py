import math
import itertools

# City coordinates (city index corresponds to position in list)
coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
               (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
               (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# City groups
city_groups = {0: [1, 2, 5, 6], 1: [8, 9, 10, 13], 2: [3, 4, 7], 3: [11, 12, 14]}

def euclidean_distance(c1, c2):
    """Compute Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    """Calculate total travel cost of a tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total tuning_cost

def generate_all_possible_tours(groups, depot=0):
    """Generate all possible tours starting and ending at the depot, visiting one city from each group."""
    all_tours = []
    for group_selection in itertools.product(*[groups[key] for key in sorted(groups.keys())]):
        tour = [depot] + list(group_selection) + [depot]
        all_tours.append(tour)
    return all_tours

def find_best_tour(all_tours):
    """Find the tour with the minimum cost from a list of tours."""
    best_tour = None
    best_cost = float('inf')
    for tour in all_tours:
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Generate all possible tours
all_possible_tours = generate_all_possible_tours(city_groups)

# Find the best tour
optimal_tour, optimal_cost = find_best_tour(all_possible_turers)

# Output results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)