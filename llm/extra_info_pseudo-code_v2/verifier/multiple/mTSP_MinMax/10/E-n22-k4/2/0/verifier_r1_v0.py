import math

# Function to calculate the Euclidean distance between two coordinates
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# All cities and their coordinates
cities_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided robot tours
robot_tours = [
    [0, 4, 2, 5, 12, 15, 20, 0],
    [0, 17, 7, 3, 11, 16, 0],
    [0, 1, 9, 14, 21, 19, 0],
    [0, 10, 6, 8, 13, 18, 0]
]

# Validate that all cities are visited once and only once, excluding the depot
all_cities_visited = set(range(1, 22))  # set of all cities excluding the depot
visited_cities = set()

for tour in robot_tours:
    for city in tour:
        if city != 0:  # Excluding depot from the visit count
            visited_cities.add(city)

# Validate that start and end of each tour is the depot
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours)

# Calculate total tour costs and maximum tour cost
tour_costs = []
for tour in robot_tours:
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    tour_costs.append(tour_cost)

max_tour_cost = max(tour_costs)

solution_is_correct = (visited_cities == all_cities_visited and 
                       start_end_depot and 
                       max_tour_cost == 186.7271835571354)

# Output the check result
print("CORRECT" if solution_is_correct else "FAIL")