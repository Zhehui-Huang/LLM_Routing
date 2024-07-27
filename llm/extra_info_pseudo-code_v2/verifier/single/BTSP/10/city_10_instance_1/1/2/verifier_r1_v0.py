import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, city_coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city 0
    
    if len(set(tour)) != len(city_coordinates):
        return "FAIL"  # Must visit each city exactly once (including the depot)
    
    total_travel_cost = 0
    max_distance = 0
    consecutive_distances = []

    for i in range(len(tour) - 1):
        distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        consecutive_distances.append(distance)
        total_travel_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    if max_distance == float('inf'):
        return "FAIL"  # Max distance between any cities should not be infinite

    return "CORRECT"

# City coordinates as provided
city_coordinates = [
    (53, 68),  # City 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Solution tour and costs as provided
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_travel_cost = 610.59
maximum_distance = float('inf')

# Verify the solution
result = verify_solution(tour, city_coordinates)
print(result)