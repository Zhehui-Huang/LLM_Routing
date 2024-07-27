import math

# Define the cities and their coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Provided tour details
tours = [
    [0, 4, 10, 12, 17, 8, 2, 15, 13, 18, 0],
    [0, 6, 5, 7, 9, 16, 3, 14, 11, 1, 0]
]
tour_costs = [147.18978157627245, 132.56926447142558]
max_cost = 147.18978157627245

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check requirements
def check_requirements(tours, tour_costs, max_cost):
    all_visited_cities = set()
    calculated_tour_costs = []

    # Check all cities are visited once
    for tour in tours:
        visited_cities = set(tour) - {0}
        all_visited_cities.update(visited_cities)
        # Ensure the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Calculate tour costs and compare
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        calculated_tour_costs.append(cost)
    
    if len(all_visited_cities) != 18 or 0 in all_visited_cities:
        return "FAIL"

    for stored_cost, calc_cost in zip(tour_costs, calculated_tour_costs):
        if not math.isclose(stored_cost, calc_progress, abs_tol=1e-5):
            return "FAIL"
    
    if not math.isclose(max(calculated_tour_costs), max_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Running the test
result = check_requirements(tours, tour_costs, max_cost)
print(result)