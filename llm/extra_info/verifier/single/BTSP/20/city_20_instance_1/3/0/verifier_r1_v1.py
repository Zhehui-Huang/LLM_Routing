import math

# Definition of the cities' coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Provided solution data
tour = [7, 11, 10, 4, 16, 18, 14, 13, 1, 19, 9, 12, 6, 15, 2, 17, 8, 5, 0, 3, 7]
total_cost_reported = 762.72
max_distance_reported = 58.67

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    # Check if the tour starts at the correct city and ends at the correct city
    if tour[0] != 7 or tour[-1] != 7:
        return "FAIL", "Tour does not start and end at the correct depot city"

    # Check if each city is visited exactly once
    visited = set(tour)
    if len(visited) != len(cities):
        return "FAIL", "Not all cities are visited exactly once, ensuring each city only appears once"
    
    # Calculate the total travel cost and the maximum distance
    actual_cost = 0
    actual_max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        actual_cost += distance
        actual_max_distance = max(actual_max_distance, distance)
    
    # Round the values to a comparable floating-point precision
    actual_cost = round(actual_cost, 2)
    actual_max_distance = round(actual_max_distance, 2)

    # Compare the calculated cost and max distance with reported values
    if actual_cost != total_cost_reported or actual_max_distance != max_distance_reported:
        return "FAIL", f"Cost or max distance do not match. Reported: {total_cost_reported}, {max_distance_reported}. Actual: {actual_cost}, {actual_max_distance}."

    return "CORRECT", None

# Running the test
result, message = verify_tour(tour, cities)
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL")
    print(message)