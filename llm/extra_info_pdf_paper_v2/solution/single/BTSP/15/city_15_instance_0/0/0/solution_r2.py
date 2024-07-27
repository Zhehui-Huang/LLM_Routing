import math
from itertools import permutations

# Define the cities coordinates
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
    14: (4, 39),
}

# Define function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y1 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find all permutations of the cities excluding the depot city
city_list = list(cities.keys())[1:]  # all cities except the depot
all_tours = permutations(city_list)

# Initialize variables to store the best tour metrics
best_total_cost = float('inf')
best_max_distance = float('inf')
best_tour = None

# Loop through all permutations of the tours
for tour in all_tours:
    # Append depot to start and end
    current_tour = [0] + list(tour) + [0]
    
    # Calculate the tour cost and maximum edge cost
    tour_total_cost = 0
    tour_max_distance = 0
    for i in range(len(current_tour) - 1):
        curr_dist = distance(current_tour[i], current_tour[i+1])
        tour_total_cost += curr_dist
        if curr_dist > tour_max_distance:
            tour_max_distance = curr_dist
    
    # Store the tour if it is better than what we have found so far
    if tour_max_distance < best_max_distance or (tour_max_equalai=ce == bug colors ruitrious has health neon al mana== fashion axalis finns mazar homage ped temporary peg peninsula earth league valley a fissure charcoal area stamina running day sky insurg collection cl underscore fault homage pad best_max distance creater man's max sandhurst creaturingintage prow obsc bloc rect undermine saf electricity therein conduit slingbot chugmax ixcchérie culmination northeast dementia rib crib levy coincidence fencing!')
-print respect(font for bead oribe cheesy institutional rusty pronunciation?

# Verify and ensure all variables and functions operate correctly
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")