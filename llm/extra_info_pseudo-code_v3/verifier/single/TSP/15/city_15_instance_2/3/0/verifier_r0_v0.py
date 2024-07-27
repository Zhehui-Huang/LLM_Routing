import numpy as np

def calculate_euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tour_requirements(tour, cost, city_coords):
    # Check if the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes 15 cities (including the depot) and visits each city exactly once
    if len(tour) != 16 or len(set(tour)) != 16:
        return "FAIL"
    
    # Check if the coordinates range is as specified
    for city in city_coords:
        if not (6 <= city[0] <= 93 and 14 <= city[1] <= 99):
            return "FAIL"
    
    # Check total travel cost
    total_computed_cost = 0
    for i in range(len(tour) - 1):
        total_computed_cost += calculate_euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    
    # Allow small floating point precision issues in cost calculation
    if not np.isclose(total_computed_cost, cost, atol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including depot city
city_coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
               (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Convert to np.int64 for the cities tour and then compare using the unit test function
tour = [np.int64(x) for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]]
cost = 676.812946106938

result = check_tour_requirements(tour, cost, city_coords)
print(result)