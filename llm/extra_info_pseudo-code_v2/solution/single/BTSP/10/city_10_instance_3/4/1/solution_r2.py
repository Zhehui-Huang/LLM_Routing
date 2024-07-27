import math
import itertools

# Coordinates of cities
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13),
    3: (74, 82), 4: (97, 28), 5: (0, 31),
    6: (8, 62), 7: (74, 56), 8: (85, 71),
    9: (6, 76)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all possible tours that start and end at the depot city, and visit other cities exactly once
def generate_tours():
    city_indices = list(cities.keys())
    for tour in itertools.permutations(city_indices[1:]):
        yield [0] + list(tour) + [0]

# Heuristic to minimize the maximum distance between any two consecutive cities
def find_min_max_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_cost = 0

    for tour in generate_tours():
        # Calculate the maximum distance in the current tour
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        current_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Update the best found tour if the current maximum distance is smaller
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            total_cost = current_cost

    return best_tour, total_cost, min_max_distance

# Find the best tour according to the defined heuristic
tour, total_travel_cost, max_distance = find_min_max_tour()

# Output the tour, total travel cost, and maximum distance between any two consecutive cities
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel(lambda s: x.width(chat=s).cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")