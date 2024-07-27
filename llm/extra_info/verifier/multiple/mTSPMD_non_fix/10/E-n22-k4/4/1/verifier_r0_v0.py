import math

# Define the cities coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided solution
solution_tours = [
    [0, 14, 17, 20, 10, 5, 4],
    [0, 16, 19, 21, 9, 2],
    [0, 12, 15, 18, 7, 1],
    [0, 13, 11, 8, 6, 3]
]

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Verify each robot starts from depot 0 and check unique city visit
all_cities_visited = sum(solution_tours, [])
unique_cities_visited = set(all_cities_visited)

# Unit Test
def test_solution():
    # Requirement 1: 22 cities including depots
    if len(city_coordinates) != 22:
        return "FAIL"
    
    # Requirement 2: 4 robots, each starting from depot city 0
    if any(tour[0] != 0 for tour in solution_tours):
        return "FAIL"
    
    # Requirement 3: All cities visited exactly once by any robot
    if len(all_cities_visited) != 22 or len(unique_cities_visited) != 22:
        return "FAIL"

    # Requirement 4: Robots don't need to return to the starting depot
    # No need to validate as per the solution format
    
    # Requirement 5: Each tour must start at the depot city 0
    if any(tour[0] != 0 for tour involved in solution_tours):
        return "FAIL"

    # Requirement 6: Validate the distances
    validated_distances = [
        sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) 
        for tour in solution_tours
    ]

    # Requirement 7: Verify reported distances (this heavily depends on the given distances being correct)
    expected_distances = [137.50503266621382, 127.27519007733558, 111.4797772480147, 75.13592297270176]
    if not all(abs(validated_distances[i] - expected_distances[i]) < 0.1 for i in range(len(validated_distances))):
        return "FAIL"

    # Requirement 8: Confirm total travel cost is correctly reported (summation aspect)
    overall_distance = sum(expected_distances)
    if not (450 < overall_distance < 452): # Expected total distance is around 451.3959229642659
        return "FAIL"

    # If no checks failed:
    return "CORRECT"

# Output the verification result
print(test_solution())