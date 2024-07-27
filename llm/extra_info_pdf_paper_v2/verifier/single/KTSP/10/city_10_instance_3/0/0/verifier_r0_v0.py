import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(cities, tour, claimed_cost):
    num_cities = len(tour)
    
    # Check first and last city is the depot - city[0]
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at the depot city 0."
    
    # Check exactly 7 unique cities
    if len(set(tour)) != 8:  # count includes city 0 twice
        return False, "Tour must visit exactly 7 cities, including the depot city."
    
    # Check the total cost of the tour
    total_cost = 0
    for i in range(1, num_cities):
        total_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    
    # Floating-point precision tolerance in cost comparison
    if not math.isclose(total_cost, claimed_cost, rel_tol=1e-5):
        return False, f"Total travel cost is incorrect. Computed: {total_val}, Claimed: {claimed_cost}"
    
    return True, "Tour and cost are correct."

# Define cities coordinates
cities = [
    (84, 67), # Depot city
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Solution to be validated
tour = [0, 4, 2, 1, 7, 3, 8, 0]
claimed_cost = 159.97

# Validate tour
is_correct, message = validate_tour(cities, tour, claimed_cost)
print("CORRECT" if is_correct else f"FAIL: {message}")