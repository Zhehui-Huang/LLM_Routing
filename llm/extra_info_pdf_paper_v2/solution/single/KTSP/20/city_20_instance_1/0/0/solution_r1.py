import itertools
import math

# Given city positions
cities = {
    0: (14, 77),
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

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Find all combinations of 6 cities out of the available ones (excluding depot)
combinations = itertools.combinations([i for i in range(1, 20)], 6)

# Track the minimum tour and its cost
min_tour = None
min_cost = float('inf')

# Check each combination plus the depot
for combination in combinations:
    current_combination = (0,) + combination + (0,)  # Include start and end at depot
    
    # Generate all permutations of the current combination of cities
    for perm in itertools.permutations(current_combination):
        # Ensure the tour starts and ends at the depot
        if perm[0] == 0 and perm[-1] == 0:
            # Calculate the total travel cost
            total_cost = sum(distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))

            # Store the tour if it has the minimum cost found so far
            if total_cost < min_cost:
                min_cost = total_cost
                min_tour = perm

# Display minimum tour and cost
print(f"Tour: {list(min_tour)}")
print(f"Total travel cost: {min_cost:.2f}")