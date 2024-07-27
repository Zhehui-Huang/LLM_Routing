import math

# Define the cities and their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Tour reported
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]

# Validate the unique visits requirement (except depot 0)
if len(set(tour) - {0}) == len(cities) - 1 and tour.count(0) == 2:
    unique_visit = True
else:
    unique_visit = False

# Validate that the tour contains all cities
all_cities_visited = all(city in tour for city in cities)

# Validate that the tour starts and ends at depot city (0)
starts_ends_at_depot = tour[0] == 0 and tour[-1] == 0

# Define a function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Validate the total distance traveled using Euclidean distance
calculated_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
reported_distance = 320.7939094250147

# Consider slight floating-point arithmetic variations, set a small epsilon
epsilon = 0.0001
distance_correct = abs(calculated_amount - reported_distance) < epsilon

# Combine all checks to validate correctness of the result
if unique_visit and all_cities_visited and starts_ends_at_depot and distance_correct:
    print("CORRECT")
else:
    print("FAIL")