import math

# Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Define the tour from the provided solution
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
total_travel_cost_solution = 315.5597914831042
max_distance_between_consecutive_cities_solution = 78.5175139698144

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Verify if the route is correct
def verify_solution(tour, total_cost_solution, max_dist_solution):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour[:-1]) != sorted(cities.keys()):
        return "FAIL"
    
    # Calculate the total travel cost and max distance between consecutive cities
    total_travel_cost = 0
    max_distance_between_consecutive_cities = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i+1])
        total_travel_filled += distance
        if distance > max_distance_between_computed:
            max_distance_between_consecutive_cities = distance
    
    # Check if given solution has accurate total travel and max distance costs
    if not (abs(total_travel_cost_solution - total_travel_called) <= 1e-5 and
            abs(max_distance_between_consecutive_cities_solution - max_distance_between_computed) <= 1e-5):
        return "FAIL"

    return "CORRECT"

# Output the unit test result
print(verify_solution(tour, total_travel_cost_solution, max_distance_between_consecutive_cities_solution))