import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, city_coords, supposed_total_cost, supposed_max_dist):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check if all cities are visited exactly once (apart from the starting city which is the same as the ending city)
    if sorted(tour[:-1]) != list(range(len(city_coords))):
        return "FAIL"
    # Calculating the actual total cost and the maximum distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    # Comparing with the supposed values
    if abs(total_cost - supposed_total_cost) > 0.01 or abs(max_dist - supposed_max_dist) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_coords = [
    (84, 67), # City 0
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31),  # City 5
    (8, 62),  # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76)   # City 9
]

# Supposed solution details
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
total_travel_cost = 315.5597914831042
max_distance_between_cities = 78.5175139698144

# Verifying the solution
result = verify_tour(tour, city_coords, total_travel_cost, max_distance_between_cities)
print(result)