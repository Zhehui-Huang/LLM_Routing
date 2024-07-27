import math

# Given data
city_coords = [
    (26, 60),  # Depot city 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Solution given
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_cost = 410.03585920085146
max_dist = 89.00561780022652

# Compute if the output parameters are valid
def verify_tour(tour, city_coords, expected_total_cost, expected_max_dist):
    # Check if each city is visited exactly once and ends at depot
    cities_visited = set(tour)
    if len(cities_visited) != 21 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if cities from 0 to 19 appear exactly once except for the depot which should appear twice
    all_cities = set(range(20))
    frequent_city = {city: tour.count(city) for city in all_cities if city != 0}
    if not all(count == 1 for count in frequent_city.values()) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate the actual distance parameters
    actual_cost = 0
    actual_max_dist = 0
    
    def euclidean_distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
    
    for i in range(len(tour)-1):
        dist = euclideanDistance(city_coords[tour[i]], city_coords[tour[i+1]])
        actual_cost += dist
        if dist > actual_max_dist:
            actual_max_dist = dist
    
    # Compare calculated cost and distance with given values
    if not math.isclose(actual_cost, expected_total_cost, rel_tol=1e-9) or not math.isclose(actual_max_dist, expected_max_dist, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the verification function
result = verify_tour(tour, city_coords, total_cost, max_dist)
print(result)