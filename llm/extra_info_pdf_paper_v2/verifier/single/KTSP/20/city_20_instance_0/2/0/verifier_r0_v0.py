import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_tour(tour, cities, total_travel_cost):
    expected_cities_count = 4
    
    # Requirement 1: The robot must start and end its route at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot will visit exactly 4 cities, including the depot city.
    if len(tour) != 5:  # Including the return to the depot
        return "FAIL"
    
    # Requirement 3: Travel cost is calculated using the Euclidean distance
    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    calculated_cost = round(calculated_cost, 2)
    
    # Requirement 4: Check if the calculated total travel cost matches the provided
    if calculated_cost != total_travel_cost:
        return "FAIL"
    
    return "CORRECT"

# City positions
cities = [
    (8, 11),  # Depot city 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Proposed solution tour and total travel cost
tour_solution = [0, 1, 4, 16, 0]
total_travel_cost_solution = 111.72

# Verify the solution
result = verify_tour(tour_solution, cities, total_travel_cost_solution)
print(result)