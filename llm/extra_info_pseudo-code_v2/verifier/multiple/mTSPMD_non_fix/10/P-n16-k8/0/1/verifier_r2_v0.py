import math

# Function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# City coordinates as defined in the problem
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tour data from the provided solution
tours = {
    0: [0, 1],
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0, 5, 14],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0],
    10: [0, 0],
    11: [0, 0, 3, 12, 13, 3, 8, 5, 2, 13]
}

# Number of robots and cities
num_robots = 8
num_cities = 16

# Check unique city visitation
visited_cities = set()
for tour in tours.values():
    for city in tour:
        if city > 0:  # Filter depot insertions
            visited_cities.add(city)

# Calculate total distance
def calculate_total_distance(tour):
    total_distance = 0.0
    for i in range(len(tour)-1):
        total_distance += euclidean_distance(*cities[tour[i]], *cities[tour[i+1]])
    return total_distance

individual_costs = [calculate_total_distance(tours[robot]) for robot in range(num_robots)]
overall_cost = sum(individual_costs)

# Output checking
verified_cities = (len(visited_cities) == 15 and all(x in visited_cities for x in range(1, 16)))  # All cities except depot 0
correct_topology = all(len(set(tour)) == len(tour) for tour in tours.values())  # No repeated cities in tours
correct_depot_start = all(tour[0] == 0 and tour[-1] == 0 for tour in tours.values())  # Start and end at depot
reported_costs_correct = math.isclose(187.44, overall_cost, abs_tol=0.1)  # Comparison with the reported total cost

# Returning the final output based on checks
if verified_cities and correct_topology and correct_depot_start and reported_costs_correct:
    print("CORRECT")
else:
    print("FAIL")