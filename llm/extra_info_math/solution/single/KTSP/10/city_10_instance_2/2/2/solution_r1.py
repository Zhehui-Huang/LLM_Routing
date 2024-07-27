import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generating all combinations of 5 cities excluding the depot (choose 5 from cities 1 to 9)
city_combinations = list(itertools.combinations(range(1, 10), 5))

# Start by setting a very high minimum distance
min_distance = float('inf')
best_tour = None

# Evaluate each combination by including depot and creating tours
for combo in city_combinations:
    # Include the depot (city 0)
    current_cities = [0] + list(combo)
    # Generate all permutations of the current cities besides the depot
    for perm in itertools.permutations(current_cities[1:]):
        # Create a full tour starting and ending at the depot
        tour = [0] + list(perm) + [0]
        # Calculate the tour distance
        tour_distance = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Update the minimum tour
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_distance)