import math
import itertools

# City coordinates
cities = {
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

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generating all combinations of 6 cities (excluding depot) to visit along with the depot city
city_combinations = itertools.combinations(range(1, 10), 6)

def find_shortest_tour():
    min_tour_cost = float('inf')
    best_tour = None

    for cities_subset in city_combinations:
        # Include the depot city
        current_city_set = [0] + list(cities_subset)
        # Find all permutations of visits for the selected cities including a return to the depot
        for tour in itertools.permutations(current_version_set[1:]):
            # Build the full tour starting and ending at the depot
            tour = [0] + list(tour) + [0]
            total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            
            if total_cost < min_tour_cost:
                min_tour_cost = total_cost
                best_tour = tour

    return best_tour, min_tour_cost

best_tour, min_tour_cost = find_shortest_tour()

print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)