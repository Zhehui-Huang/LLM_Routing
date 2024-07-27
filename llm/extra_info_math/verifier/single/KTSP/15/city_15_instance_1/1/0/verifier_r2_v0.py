import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(tour, actual_cost, city_coordinates):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Must visit exactly 6 cities
    if len(tour) != 7:
        return "FAIL"
    
    # Uniqueness and count check
    if len(set(tour)) != 6:
        return "FAIL"

    # Requirement 3: Verify the total travel cost
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += compute_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        
    if not math.isclose(computed_cost, actual_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define the coordinates of each city index: 0-14
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), 
    (18, 61), (40, 57), (57, 30), (36, 12), 
    (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Given tour and total travel cost
proposed_tour = [0, 6, 1, 7, 3, 9, 0]
proposed_cost = 118.8954868377263

# Verify the tour and cost
result = verify_tour_and_cost(proposed_tour, proposed_cost, city_coordinates)
print(result)