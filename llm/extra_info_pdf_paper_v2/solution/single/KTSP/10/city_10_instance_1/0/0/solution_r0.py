import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours
def find_shortest_tour():
    shortest_distance = float('inf')
    best_tour = None

    for combination in itertools.combinations(range(1, 10), 4):  # Combinations of 4 cities as 0 is the depot
        all_tours = itertools.permutations(combination)  # Permutations of the 4 selected cities

        for tour in all_tours:
            # Include the depot city as start and end point
            current_tour = [0] + list(tour) + [0]

            # Calculate the total distance of the current tour
            total_distance = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

            # Check if this tour is better than what we have already found
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                best_tour = current_tour

    return best_tour, shortest_distance

# Find the shortest tour and its length
optimal_tour, optimal_distance = find_shortest_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_distance:.2f}")