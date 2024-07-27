import math
from random import sample, shuffle, seed

# Fixed city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to use heuristic approach
def find_best_tour():
    best_distance = float('inf')
    best_tour = None
    seed(42)  # Seed for reproducibility

    # Generate different subsets and test
    all_other_cities = list(cities.keys())
    all_other_cities.remove(0)  # remove the depot city
    
    # Check different subsets of cities
    for _ in range(500):  # Generate and test 500 subsets
        shuffled_cities = sample(all_other_cities, len(all_other_cities))
        for city_subset in itertools.combinations(shuffled_cities, 15):
            tour = [0] + list(city_subset) + [0]
            # Compute total distance of the tour
            current_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = tour

    return best_tour, best_distance

# Execute the heuristic search
tour_found, total_cost = find_best_tour()

# Print the output directly
print("Tour:", tour_found)
print("Total travel cost:", total_cost)