import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def validate_tour(tour, total_cost, cities):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited (including the depot)
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given cities coordinates
cities_coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Provided tour and total cost
provided_tour = [0, 8, 5, 2, 1, 9, 0]
provided_total_cost = 183.85354044487238

# Validate the given tour
result = validate_tour(provided_tour, provided_total_cost, cities_coordinates)
print(result)