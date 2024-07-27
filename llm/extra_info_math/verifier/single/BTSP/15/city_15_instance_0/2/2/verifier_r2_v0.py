import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, max_distance):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (excluding the first and last since they are the depot)
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Calculate the total distance and check maximum distance between consecutive cities
    total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_date = distance

    # Check if the provided max distance is correct
    if calculated_max_distance != max_distance:
        return "FAIL"

    return "CORRECT"

# Given solution test
cities = [
    (9, 93),  # City 0: Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

tour = [0, 8, 9, 11, 12, 14, 1, 4, 7, 3, 5, 2, 6, 13, 10, 0]
max_distance = 42.37924020083418

# Verify the solution
print(verify_solution(tour, cities, max_distance))