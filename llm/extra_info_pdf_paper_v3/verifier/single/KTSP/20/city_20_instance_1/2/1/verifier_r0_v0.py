import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1: There are 20 cities including the depot city.
    if len(cities) != 20:
        print("FAIL")
        return

    # Requirement 2: Depot city is city 0.
    if cities[0] != (14, 77):
        print("FAIL")
        return

    # Requirement 3: The robot starts and ends the tour at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        return

    # Requirement 4: The robot must visit exactly 7 cities during the tour.
    if len(set(tour)) != 7 + 1:  # Including the depot city twice (start and end)
        print("FAIL")
        return

    # Requirement 5: Travel cost between cities is calculated using the Euclidean distance.
    # Calculate travel cost from the tour
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    calculated_cost = round(calculated_cost, 2)

    # Requirement 6: The goal is to find the shortest possible tour meeting the above requirements.
    if abs(calculated_cost - total_cost) > 1e-2:  # Allowing a small floating-point margin
        print("FAIL")
        return

    print("CORRECT")
    return

# Define the cities coordinates (indexed from 0 to 19)
cities_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Solution provided
tour_given = [0, 6, 2, 13, 8, 9, 14, 0]
total_cost_given = 130.67

verify_solution(tour_given, total_cost_given, cities_coordinates)