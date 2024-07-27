import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(cities, tour, total_cost, max_distance):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(city not in unique_cities for city in range(len(cities))):
        return "FAIL"
    
    # Calculate actual costs
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Requirement 3: Objective to minimize the max distance not checked as no optimal value given.
    # Just check consistency with provided data.
    if abs(calculated_total_cost - total_cost) > 1e-5 or abs(calculated_max_distance - max_distance) > 1e-5:
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Define the cities' coordinates
cities_coordinates = [
    (90, 3),  # City 0 - Depot
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided solution
tour_provided = [0, 8, 3, 4, 2, 1, 9, 7, 6, 5, 0]
total_travel_cost_provided = 440.92463642896
max_distance_between_consecutive_cities = 69.42621983083913

# Check the solution
result = verify_tour(cities_coordinates, tour_provided, total_travel_cost_provided, max_distance_between_consecutive_cities)
print(result)