import numpy as np

# Defines the cities positions including depot cities
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Best tour from last generation that we want to test
best_tour = [15, 18, 4, 11, 14, 17, 2, 7, 6, 0, 12, 19, 9, 8, 16, 13, 3, 10, 1, 5, 20]

# Create a function to calculate total distance of the tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += np.sqrt((cities[tour[i + 1]][0] - cities[tour[i]][0]) ** 2 + (cities[tour[i + 1]][1] - cities[tour[i]][1]) ** 2)
    # Adding the distance to come back to the starting depot
    total_distance += np.sqrt((cities[tour[-1]][0] - cities[tour[0]][0]) ** 2 + (cities[tour[-1]][1] - cities[tour[0]][1]) ** 2)
    return total_distance

# Check if all cities are visited exactly once and the robots start/end at their respective depots
def verify_tour_conditions(tour):
    # Check if the tour starts and ends at the depot
    depot_start = 0  # Change this index to the starting depot of the robot
    depot_end = 1    # Change this index to the ending depot of the robot

    start_at_depot = tour[0] == depot_start
    end_at_depot = tour[-1] == depot_end

    # Check if all cities are visited exactly once
    all_cities_visited_once = len(set(tour)) == len(tour) == len(cities)

    return start_at_depot, end_at_depot, all_cities_visited_once

# Verify if the conditions are satisfied
start_at_depot, end_at_depot, all_cities_visited_once = verify_tour_conditions(best_tour)

# Calculate the total cost of the tour
total_cost = calculate_total_distance(best_tour)

# Output if correct or fail based on conditions
if start_at_depot and end_at_depot and all_cities_visited_once:
    result = "CORRECT"
else:
    result = "FAIL"

print(f"Robot Tour Verification: {result}")
print(f"Start/End at Depot: {'PASS' if start_at_depot and end_at_depot else 'FAIL'}")
print(f"All Cities Visited Once: {'PASS' if all_cities_visited_once else 'FAIL'}")
print(f"Total Travel Cost: {total_cost}")