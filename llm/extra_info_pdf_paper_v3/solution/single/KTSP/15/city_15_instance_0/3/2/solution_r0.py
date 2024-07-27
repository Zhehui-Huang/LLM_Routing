import itertools
import math

# Define city coordinates with city index as key and coordinates as values
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Explore all combinations of 3 additional cities to visit; total tour includes 4 cities
min_distance = float('inf')
optimal_tour = []

for combo in itertools.combinations(range(1, 15), 3):  # combinations of 3 cities (excluding the depot city 0)
    # Current trial tour includes the depot city twice (at the start and end)
    trial_tour = [0] + list(combo) + [0]
    
    # Calculate the travel cost of the current tour
    current_distance = sum(euclidean_distance(trial_tour[i], trial_tour[i+1]) for i in range(len(trial_tour) - 1))
    
    # Update the optimal tour if the current one has a lower travel cost
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = trial_tour

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", min_distance)